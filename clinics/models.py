from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import FieldPanel


@register_snippet
class Catogories(models.Model):
    """Speciality Catogories eg Pediatric Neurology, Epilepsy, Neurology
    all under Neurology
    """

    catogory_name = models.CharField(max_length=50)
    panels = [
        FieldPanel("catogory_name"),
    ]

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.catogory_name


@register_snippet
class Clinics(models.Model):
    """Clinics"""

    clinic_name = models.CharField(max_length=100)
    clinic_catogory_id = models.ForeignKey(Catogories, on_delete=models.CASCADE)

    panels = [
        FieldPanel("clinic_name"),
        FieldPanel("clinic_catogory_id"),
    ]

    class Meta:
        verbose_name = "Clinic"
        verbose_name_plural = "Clinics"

    def __str__(self):
        return self.clinic_name


@register_snippet
class Rooms(models.Model):
    """Clinic Room Numbers"""

    room_number = models.CharField(max_length=30)
    panels = [
        FieldPanel("room_number"),
    ]

    class Meta:
        verbose_name = " Room Number"
        verbose_name_plural = "Room Numbers"

    def __str__(self):
        return self.room_number


@register_snippet
class ClinicRoom(models.Model):
    """Clinic Room"""

    days_choice = [
        ("Mon", "Monday"),
        ("Tue", "Tuesday"),
        ("Wed", "Wednesday"),
        ("Thu", "Thursday"),
        ("Fri", "Friday"),
        ("Sat", "Saturday"),
        ("Wee", "Weekday"),
    ]
    time_choice = [
        ("morning", "8-12am"),
        ("evening", "2-4pm"),
        ("day", "8am - 4pm"),
    ]
    clinic_id = models.ForeignKey(Clinics, on_delete=models.CASCADE)
    weekday = models.CharField(max_length=50, choices=days_choice)
    clinic_time = models.CharField(max_length=50, choices=time_choice)
    room_no = models.ForeignKey(Rooms, on_delete=models.CASCADE)

    panels = [
        FieldPanel("clinic_id"),
        FieldPanel("weekday"),
        FieldPanel("clinic_time"),
        FieldPanel("room_no"),
    ]

    def __str__(self):
        return self.clinic_id.__str__()


@register_snippet
class Speciality(models.Model):
    """Speciality for Consultants & Clinics"""

    speciality_type = models.CharField(max_length=100)
    panels = [
        FieldPanel("speciality_type"),
    ]

    class Meta:
        verbose_name = "Speciality"
        verbose_name_plural = "Specialities"

    def __str__(self):
        return self.speciality_type


@register_snippet
class Consultant(models.Model):
    """Consultant Detail for Clinics"""

    consultant_name = models.CharField(max_length=200)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    clinic_id = models.ManyToManyField(Clinics)
    panels = [
        FieldPanel("consultant_name"),
        FieldPanel("speciality"),
        FieldPanel("clinic_id"),
    ]

    def __str__(self):
        return self.consultant_name
