# -*- coding: utf-8 -*-
"""Helper models."""
class Permission:
  LOGIN = 0x01
  EDITOR = 0x02
  OPERATOR = 0x04
  ADMINISTER = 0xFF

  PERMISSION_MAP = {
      LOGIN: ("login", "Login user"),
      EDITOR: ("editor", "Editor"),
      OPERATOR: ("op", "Operator"),
      ADMINISTER: ("admin", "Super administrator"),
    }