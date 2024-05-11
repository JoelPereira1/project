# -*- coding: utf-8 -*-
"""Helper routes."""
import functools
from datetime import timedelta
from werkzeug.utils import secure_filename
from settings import Config
from shop.constant import ALLOWED_EXTENSIONS
from minio import Minio
import os
from flask import current_app

def get_unique_path(path):
  parent = path.parent
  if path.exists():
    name = path.stem
    ext = path.suffix
    i = 1
    while True:
      new_path = parent / f"{name}({i}){ext}"
      if not new_path.exists():
        return new_path
      i += 1
  else:
      return path

# TODO| Change to fileserver location
def save_img_file(image):
  client = Minio(Config.MINIO_API_HOST, Config.MINIO_ACCESS_KEY, Config.MINIO_SECRET_KEY, secure=False)
  # Make bucket if not exist.
  found = client.bucket_exists(Config.BUCKET_NAME)
  if not found:
    client.make_bucket(Config.BUCKET_NAME)
  else:
    print(f"Bucket {Config.BUCKET_NAME} already exists")

  size = os.fstat(image.fileno()).st_size
  # Upload data.
  result = client.put_object(Config.BUCKET_NAME, image.filename, image, size)
  print(
    "created {0} object; etag: {1}, version-id: {2}".format(
        result.object_name, result.etag, result.version_id,
    )
  )

  url = client.get_presigned_url('GET' ,Config.BUCKET_NAME, image.filename, expires=timedelta(hours=2))
  background_img_url = url
  print(background_img_url)

  # upload_path = current_app.config["UPLOAD_DIR"] / image.filename
  # upload_path = get_unique_path(upload_path)
  # upload_path.write_bytes(image.read())
  # background_img_url = upload_path.relative_to(
  #   current_app.config["STATIC_DIR"]
  # ).as_posix()

  return background_img_url

def wrap_partial(fn, *args, **kwargs):
  partial_func = functools.partial(fn, *args, **kwargs)
  functools.update_wrapper(partial_func, args[0])
  return partial_func

def item_del(cls, id):
  try:
    item = cls.get_by_id(id)
    item.delete()
  except Exception as e:
    return {"code": 1, "msg": str(e)}
  return {"code": 0}

def allowed_file(filename):
  return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS