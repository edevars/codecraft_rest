from newsletter.models import Template, Suscriptor
from django.core.mail import EmailMessage, get_connection
from django.conf import settings

def send_email(template_id, recipients):
  try:
    template = Template.objects.get(pk=template_id)
    suscriptors = recipients
    if not suscriptors:
      suscriptors = Suscriptor.objects.filter(suscribed=True)
    
    subject = template.subject
    content = template.content
    file_path = template.attached_file.path
    success_emails = []
    messages = []

    for suscriptor in suscriptors:
      message = EmailMessage(
        subject=subject,
        body=content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[suscriptor.email],
      )

      if file_path:
        message.attach_file(file_path)

      messages.append(message)

    for message in messages:
      message.send()
      success_emails.append(message.to)

    return success_emails
  except Template.DoesNotExist:
    raise ValueError('Template does not exist')
  except Exception as e:
    raise e