from flask import session
from flask_babel import lazy_gettext as _l
from wtforms import PasswordField, SelectField, StringField, TextAreaField
from wtforms.fields.html5 import DateField, URLField

from CTFd.constants.languages import SELECT_LANGUAGE_LIST
from CTFd.forms import BaseForm
from CTFd.forms.fields import SubmitField
from CTFd.forms.users import attach_custom_user_fields, build_custom_user_fields
from CTFd.utils.countries import SELECT_COUNTRIES_LIST
from CTFd.utils.user import get_current_user


def SettingsForm(*args, **kwargs):
    class _SettingsForm(BaseForm):
        name = StringField(_l("User Name"))
        email = StringField(_l("Email"))
        language = SelectField(_l("Language"), choices=SELECT_LANGUAGE_LIST)
        password = PasswordField(_l("Password"))
        confirm = PasswordField(_l("Current Password"))
        affiliation = StringField(_l("Affiliation"))
        website = URLField(_l("Website"))
        country = SelectField(_l("Country"), choices=SELECT_COUNTRIES_LIST)
        submit = SubmitField(_l("Submit"))

        @property
        def extra(self):
            fields_kwargs = _SettingsForm.get_field_kwargs()
            return build_custom_user_fields(
                self,
                include_entries=True,
                fields_kwargs=fields_kwargs,
                field_entries_kwargs={"user_id": session["id"]},
            )

        @staticmethod
        def get_field_kwargs():
            user = get_current_user()
            field_kwargs = {"editable": True}
            if user.filled_all_required_fields is False:
                # Show all fields
                field_kwargs = {}
            
            field_kwargs["set_only_by_admin"] = False
            return field_kwargs

    field_kwargs = _SettingsForm.get_field_kwargs()
    attach_custom_user_fields(_SettingsForm, **field_kwargs)

    return _SettingsForm(*args, **kwargs)


class TokensForm(BaseForm):
    expiration = DateField(_l("Expiration"))
    description = TextAreaField("Usage Description")
    submit = SubmitField(_l("Generate"))
