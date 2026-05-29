from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('candidate', 'Кандидат'),
        ('hr_manager', 'HR-менеджер'),
        ('admin', 'Администратор'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='candidate',
        verbose_name='Роль'
    )

    def __str__(self):
        return f'{self.username} ({self.get_role_display()})'

    @property
    def is_candidate(self):
        return self.role == 'candidate'

    @property
    def is_hr_manager(self):
        return self.role == 'hr_manager'

    @property
    def is_admin(self):
        return self.role == 'admin' or self.is_superuser

class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    experience = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.position}"


