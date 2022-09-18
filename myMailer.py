from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key[
    "api-key"
] = "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"

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
    sib_api_v3_sdk.ApiClient(configuration)
)


def MailSender(props):
    subject, sender, reply_to, html_content, to, params, headers, cc, bcc =props.values()
    # subject = "from the Python SDK!"
    # sender = {"name":"Ritesh Patel","email":"riteshp112@gmail.com"}
    # reply_to = {"name":"Ritesh Patel","email":"riteshp112@gmail.com"}
    # html_content = "<html><body><h1>This is my first transactional email </h1></body></html>"
    # to = [{"email":"4bhis1@gmail.com","name":"Abhishek Kumar"}]
    # params = {"parameter":"My param value","subject":"New Subject"}
    print(props,subject,sender,params,reply_to,to)
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to,
        # bcc=bcc,
        # cc=cc,
        reply_to=reply_to,
        # headers=headers,
        html_content=html_content,
        sender=sender,
        subject=subject,
    )
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        return api_response
    except ApiException as e:
        return "Exception when calling SMTPApi->send_transac_email:" + str(e)
