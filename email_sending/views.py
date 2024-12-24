from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactSerializer
from .utils import send_custom_email
from .models import SMTPSettings


class ContactView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            phone = serializer.validated_data['phone']
            company = serializer.validated_data['company']
            message = serializer.validated_data.get('message', '')

            try:
                smtp_settings = SMTPSettings.objects.first()

                if not smtp_settings:
                    return Response(
                        {
                            'error': 'SMTP settings are not configured in the admin panel.'
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

                admin_subject = f'New Contact Form Submission from {name}'
                admin_message = (
                    f"Name: {name}\n"
                    f"Email: {email}\n"
                    f"Phone: {phone}\n"
                    f"Company: {company}\n"
                    f"Message: {message}"
                )
                send_custom_email(admin_subject, admin_message, recipient_list=[smtp_settings.admin_email])

                user_subject = 'We have received your request!'
                user_message = (
                    f"Hi {name},\n\n"
                    "Thank you for reaching out to us. We have received your request and will get back to you shortly.\n\n"
                    "Best regards,\nYour Company"
                )
                send_custom_email(user_subject, user_message, recipient_list=[email])

                return Response({'success': 'Message sent successfully!'}, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
