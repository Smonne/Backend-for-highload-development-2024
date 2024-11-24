from django.db import models
from encrypted_fields import EncryptedCharField

# class Email(models.Model):
#     recipient = models.EmailField()
#     subject = models.CharField(max_length=255)
#     body = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.subject
    

class SecureModel(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    sensitive_data = EncryptedCharField(max_length=255)


    def __str__(self):
        return self.name
    
class DataUpload(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Completed', 'Completed')], default='Pending')

    def __str__(self):
        return f"Upload by {self.user.username} at {self.uploaded_at}"

   
