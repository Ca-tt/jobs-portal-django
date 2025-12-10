
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Vacancy(models.Model):
    company = models.CharField(max_length=255)
    position_title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    employment_type = models.CharField(
        max_length=50,
        choices=[
            ("full_time", "Full Time"),
            ("part_time", "Part Time"),
            ("contract", "Contract"),
            ("internship", "Internship"),
            ("temporary", "Temporary"),
            ("remote", "Remote"),
            ("other", "Other"),
        ],
        default="full_time",
    )
    salary_from = models.PositiveIntegerField(null=True, blank=True)
    salary_to = models.PositiveIntegerField(null=True, blank=True)
    salary_note = models.CharField(max_length=100, default="Not stated")
    
    url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    active_until = models.DateField()
    
    job_description = models.TextField(help_text="HTML allowed for formatting")

    experience_required = models.CharField(max_length=100, blank=True, help_text="E.g. '2+ years', 'Entry level'")
    education_level = models.CharField(
        max_length=50,
        choices=[
            ("none", "No formal education"),
            ("high_school", "High School"),
            ("associate", "Associate Degree"),
            ("bachelor", "Bachelor's Degree"),
            ("master", "Master's Degree"),
            ("doctorate", "Doctorate/PhD"),
            ("other", "Other"),
        ],
        default="none",
        blank=True,
        help_text="Minimum education required"
    )
    industry = models.CharField(max_length=100, blank=True, help_text="Industry or sector, e.g. 'IT', 'Finance'")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    icon_id = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Random icon id from 1 to 10"
    )

    class Meta:
        ordering = ["-publish_date"]

    def __str__(self):
        return f"{self.position_title} at {self.company}"
