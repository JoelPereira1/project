from flask_wtf import FlaskForm as _FlaskForm
from flask_wtf.file import FileSize, FileAllowed
from wtforms import (
    BooleanField,
    DateTimeField,
    DateField,
    DecimalField,
    FieldList,
    FileField,
    MultipleFileField,
    FloatField,
    IntegerField,
    PasswordField,
    RadioField,
    SelectField,
    SelectMultipleField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import DataRequired, Length, NumberRange, Regexp, optional
from shop.constant import SettingValueType
from shop.models.utils import Permission

class FlaskForm(_FlaskForm):
    def validate(self, extra_validators=None):
        self._errors = None
        success = True
        for name, field in self._fields.items():
            if field.type in (
                "SelectField",
                "SelectMultipleField",
                "RadioField",
                "FieldList",
            ):
                continue
            if extra_validators is not None and name in extra_validators:
                extra = extra_validators[name]
            else:
                extra = tuple()
            if not field.validate(self, extra):
                success = False
        return success

class DashboardMenuForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    order = IntegerField("Order", default=0)
    endpoint = StringField("End Point")
    icon_cls = StringField("Icon")
    parent_id = SelectField("Parent")
    submit = SubmitField("Submit")


class SiteMenuForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    order = IntegerField("Order", default=0)
    url_ = StringField("Url")
    parent_id = SelectField("Parent")
    position = RadioField(
        "Position",
        choices=[
            (0, "none"),
            (1, "top"),
            (2, "bottom"),
        ],
        default=0,
    )
    category_id = SelectField("Category")
    collection_id = SelectField("Collection")
    page_id = SelectField("Page")
    submit = SubmitField("Submit")


class SitePageForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    slug = StringField(
        "Slug",
        validators=[Regexp(r"^\D+$", message="slug can not be number")],
    )
    content = StringField("Content")
    is_visible = BooleanField("Is Visible", default=True)
    submit = SubmitField("Submit")


class SiteConfigForm(FlaskForm):
    header_text = StringField("Header", validators=[DataRequired()])
    description = TextAreaField("Description")
    submit = SubmitField("Submit")


class UserForm(FlaskForm):
    username = StringField("User Name", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired()])
    password = PasswordField("Password")
    is_active = BooleanField("Is Active")
    role = SelectField(
        "Role",
        coerce=str,
        choices=list(Permission.PERMISSION_MAP.values()),
    )
    created_at = DateTimeField("Created at")
    updated_at = DateTimeField("Updated at")
    submit = SubmitField("Submit")


class UserAddressForm(FlaskForm):
    province = StringField("Province")
    city = StringField("Sity")
    district = StringField("District")
    address = StringField("Address")
    contact_name = StringField("Contact Name")
    contact_phone = StringField("Contact Phone")
    submit = SubmitField("Submit")


class AttributeForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    values_label = StringField(
        "Value",
        description="Multiple values need separated by ','"
    )
    product_types_ids = SelectMultipleField("Product Types")
    submit = SubmitField("Submit")


class CollectionForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    products_ids = SelectMultipleField("Products")
    background_img = StringField("Current Image")
    bgimg_file = FileField(
        "Upload a new one",
        validators=[
            FileAllowed(["jpg", "png", "gif", "jpeg"], "Images only!"),
            FileSize(1024 * 1024 * 1024, message="It is too big!"),
        ],
    )
    submit = SubmitField("Submit")


class CategoryForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    parent_id = SelectField("Parent", coerce=int, default=0)
    background_img = StringField("Current Image")
    bgimg_file = FileField(
        "Upload a new one",
        validators=[
            FileAllowed(["jpg", "png", "gif", "jpeg"], "Images only!"),
            FileSize(1024 * 1024 * 1024, message="It is too big!"),
        ],
    )
    submit = SubmitField("Submit")


class ProductTypeForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    has_variants = BooleanField("Has variant", default=True)
    is_shipping_required = BooleanField(
        "Is shipping required", default=True
    )
    product_attributes_ids = SelectMultipleField("Product atributes")
    submit = SubmitField("Submit")


class ProductForm(FlaskForm):
    title = StringField("Title")
    basic_price = DecimalField("Basic Price")
    on_sale = BooleanField("On Sale", default=True)
    is_featured = BooleanField("Is Featured", default=False)
    rating = FloatField("Rating", default=0)
    sold_count = IntegerField("Sold Count", default=0)
    review_count = IntegerField("Review Count", default=0)
    category_id = SelectField("Category")
    description = TextAreaField("Description")
    images = FieldList(StringField("Images"))
    new_images = MultipleFileField(
        "",
        validators=[
            FileAllowed(["jpg", "png", "gif", "jpeg"], "Images only!"),
            FileSize(1024 * 1024 * 1024, message="It is too big!"),
            Length(max=5, message="You can only upload 5 images once"),
        ],
    )
    attributes = FieldList(SelectField("Atributes"))
    submit = SubmitField("Submit")


class ProductCreateForm(FlaskForm):
    product_type_id = SelectField("Choose A Product Type", default=1)
    submit = SubmitField("Next")


class VariantForm(FlaskForm):
    sku_id = IntegerField(
        "SKU", validators=[DataRequired(), NumberRange(min=1, max=9999)]
    )
    title = StringField("Title", validators=[DataRequired()])
    price_override = DecimalField(
        "Price override", default=0.00, validators=[NumberRange(min=0)]
    )
    quantity = IntegerField(
        "Quantity", default=0, validators=[NumberRange(min=0)]
    )
    submit = SubmitField("Submit")


class ShippingMethodForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    price = DecimalField(
        "Price", default=0.00, validators=[NumberRange(min=0)]
    )
    submit = SubmitField("Submit")


class VoucherForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    type_ = SelectField("Type", default=1)
    code = StringField("Code", validators=[DataRequired()])
    usage_limit = IntegerField(
        "Usage limit",
        description="how many times can be used",
        validators=[optional()],
    )
    used = IntegerField("Used", default=0)
    start_date = DateField("Start At")
    end_date = DateField("End At")
    discount_value_type = SelectField("Discount value type", default=1)
    discount_value = DecimalField("Discount value", default=0.00)
    limit = IntegerField("Limit", validators=[optional()])
    category_id = SelectField(
        "Category",
        description="when type is category, need to select",
    )
    product_id = SelectField(
        "Product",
        description="when type is product, need to select",
    )
    submit = SubmitField("Submit")


class SaleForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    discount_value_type = SelectField("Discount value type", default=1)
    discount_value = DecimalField("Discount value", default=0.00)
    categories_ids = SelectMultipleField("Category", coerce=int)
    products_ids = SelectMultipleField("Product")
    submit = SubmitField("Submit")


def generate_settings_form(settings):
    """Generates a settings form which includes field validation
    based on our Setting Schema."""

    class SettingsForm(FlaskForm):
        pass

    # now parse the settings in this group
    for setting in settings:
        field_validators = []

        if setting.value_type in {SettingValueType.integer, SettingValueType.float}:
            validator_class = NumberRange
        elif setting.value_type == SettingValueType.string:
            validator_class = Length

        # generate the validators
        if setting.extra:
            if "min" in setting.extra:
                # Min number validator
                field_validators.append(validator_class(min=setting.extra["min"]))

            if "max" in setting.extra:
                # Max number validator
                field_validators.append(validator_class(max=setting.extra["max"]))

        # Generate the fields based on value_type
        # IntegerField
        if setting.value_type == SettingValueType.integer:
            setattr(
                SettingsForm,
                setting.key,
                IntegerField(
                    setting.name,
                    validators=field_validators,
                    description=setting.description,
                ),
            )
        # FloatField
        elif setting.value_type == SettingValueType.float:
            setattr(
                SettingsForm,
                setting.key,
                FloatField(
                    setting.name,
                    validators=field_validators,
                    description=setting.description,
                ),
            )

        # TextField
        elif setting.value_type == SettingValueType.string:
            setattr(
                SettingsForm,
                setting.key,
                StringField(
                    setting.name,
                    validators=field_validators,
                    description=setting.description,
                ),
            )

        # SelectMultipleField
        elif setting.value_type == SettingValueType.selectmultiple:
            # if no coerce is found, it will fallback to unicode
            if "coerce" in setting.extra:
                coerce_to = setting.extra["coerce"]
            else:
                coerce_to = str

            setattr(
                SettingsForm,
                setting.key,
                SelectMultipleField(
                    setting.name,
                    choices=setting.extra["choices"](),
                    coerce=coerce_to,
                    description=setting.description,
                ),
            )

        # SelectField
        elif setting.value_type == SettingValueType.select:
            # if no coerce is found, it will fallback to unicode
            if "coerce" in setting.extra:
                coerce_to = setting.extra["coerce"]
            else:
                coerce_to = str

            setattr(
                SettingsForm,
                setting.key,
                SelectField(
                    setting.name,
                    coerce=coerce_to,
                    choices=setting.extra["choices"](),
                    description=setting.description,
                ),
            )

        # BooleanField
        elif setting.value_type == SettingValueType.boolean:
            setattr(
                SettingsForm,
                setting.key,
                BooleanField(setting.name, description=setting.description),
            )

    SettingsForm.submit = SubmitField("Submit")
    return SettingsForm
