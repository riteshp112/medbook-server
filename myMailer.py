from __future__ import print_function
from config import MAIL_API_KEY
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from operator import itemgetter

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key["api-key"] = MAIL_API_KEY

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
    sib_api_v3_sdk.ApiClient(configuration)
)


def MailSender(params):

    subject, sender, reply_to, html_content, to, = itemgetter(
        "subject", "sender", "reply_to", "html_content", "to"
    )(params)

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to,
        reply_to=reply_to,
        html_content=html_content,
        sender=sender,
        subject=subject,
    )
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        return {"response": {"result": api_response}}
    except ApiException as e:
        return {"error": "Exception when calling SMTPApi->send_transac_email:" + str(e)}
