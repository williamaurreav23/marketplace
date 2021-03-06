from django.utils.translation import ugettext_lazy as _

from marketplace.emails.helpers import TemplateEmailMessage


class VerificationEmail(TemplateEmailMessage):
    """Email notification when when an user is register, to verify his email."""

    template_name = "emails/verification.html"
    default_subject = _("Verify your email")


class RestorePasswordEmail(TemplateEmailMessage):
    """Email notification when when an user request a restore password code."""

    template_name = "emails/restore_password.html"
    default_subject = _("Restore your password")


class ChangedPasswordEmail(TemplateEmailMessage):

    template_name = "emails/changed_password.html"
    default_subject = _("Your password has changed")


class VerifiedEmail(TemplateEmailMessage):

    template_name = "emails/verified.html"
    default_subject = _("Your account is now verified")
