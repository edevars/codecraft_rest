from newsletter.models import Template, Suscriptor
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
import markdown

def transform_content_to_html(original_content):
  content = markdown.markdown(original_content)
  return content

def custome_body(body,name=""):
  return body.replace("{{name}}",name)

def send_email(template_id, recipients):
  try:
    template = Template.objects.get(pk=template_id)
    suscriptors = recipients
    if not suscriptors:
      suscriptors = Suscriptor.objects.filter(suscribed=True)
    
    subject = template.subject
    content = transform_content_to_html(template.content)
    file_path = template.attached_file.path
    success_emails = []
    messages = []

    for suscriptor in suscriptors:
      email = ""
      name= ""
      if len(recipients) > 0:
        email = suscriptor["email"]
      else:
        email = suscriptor.email
        name = suscriptor.name
      
      custome_content = custome_body(content,name)

      message = EmailMessage(
        subject=subject,
        body=custome_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email],
      )
      message.content_subtype = 'html'

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