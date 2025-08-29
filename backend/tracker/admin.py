# backend/tracker/admin.py

from django.contrib import admin

from .models import DiaryEntry, Food, Goal


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("name", "default_unit", "calories", "protein", "carbs", "fat")
    search_fields = ("name",)
    list_filter = ("default_unit",)


@admin.register(DiaryEntry)
class DiaryEntryAdmin(admin.ModelAdmin):
    list_display = ("date", "meal_type", "food", "quantity", "unit")
    list_filter = ("meal_type", "date")
    search_fields = ("food__name",)


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("start_date", "calorie_goal", "protein_goal", "carb_goal", "fat_goal")
    list_filter = ("start_date",)
