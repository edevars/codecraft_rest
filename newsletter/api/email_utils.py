from newsletter.models import Template, Suscriptor, Newsletter
from django.core.mail import EmailMessage
from django.conf import settings
import markdown

def add_unsuscribe_link(body, email):
  unsuscribe_url = f"{settings.CODECRAFT_BASE_URL}/unsuscribe/{email}"
  link = f'<a style="color:white;" href="{unsuscribe_url}">Click here</a>'
  return f'{body}<br><br><div style="background:#4430b7;color:white;padding:16px;">If you want to unsuscribe {link}<div/>'

def transform_content_to_html(original_content):
  content = markdown.markdown(original_content)
  return content

def custom_body(body,name="", email=""):
  new_body = body.replace("{{name}}",name)
  new_body = add_unsuscribe_link(new_body, email)
  return new_body

def send_email(template_id, recipients, newsletter_name):
  try:
    template = Template.objects.get(pk=template_id)
    suscriptors = recipients
    if not suscriptors:
      suscriptors = Suscriptor.objects.filter(suscribed=True)
    
    subject = template.subject
    content = transform_content_to_html(template.content)
    file_path = None
    if template.attached_file:
      file_path = template.attached_file.path
    success_emails = []
    messages = []

    for suscriptor in suscriptors:
      tmp_suscriptor = suscriptor
      if len(recipients) > 0:
        tmp_suscriptor = Suscriptor.objects.filter(email=suscriptor["email"])
        if tmp_suscriptor.exists():
          tmp_suscriptor = Suscriptor.objects.get(email=suscriptor["email"])
          print("Existed",tmp_suscriptor)
        else:
          tmp_suscriptor = Suscriptor.objects.create(email=suscriptor["email"], name="", suscribed=True)

      name = tmp_suscriptor.name
      email = tmp_suscriptor.email
    
      custom_content = custom_body(content, name, email)

      if tmp_suscriptor.suscribed:
        message = EmailMessage(
          subject=subject,
          body=custom_content,
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
    
    Newsletter.objects.create(name=newsletter_name, template=template, count_sent=len(success_emails))

    return success_emails
  except Template.DoesNotExist:
    raise ValueError('Template does not exist')
  except Exception as e:
    raise e