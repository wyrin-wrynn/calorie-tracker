# Create your models here.
from django.db import models


class Food(models.Model):
    UNIT_CHOICES = [
        ("g", "Grams"),
        ("piece", "Piece"),
        ("slice", "Slice"),
        ("bowl", "Bowl"),
        ("cup", "Cup"),
        ("katori", "Katori"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=200, unique=True)
    default_unit = models.CharField(max_length=20, choices=UNIT_CHOICES, default="g")
    calories = models.FloatField(help_text="Calories per unit")
    protein = models.FloatField(default=0, help_text="Protein per unit (g)")
    carbs = models.FloatField(default=0, help_text="Carbs per unit (g)")
    fat = models.FloatField(default=0, help_text="Fat per unit (g)")
    fiber = models.FloatField(default=0, help_text="Fiber per unit (g)")
    sugar = models.FloatField(default=0, help_text="Sugar per unit (g)")
    sodium = models.FloatField(default=0, help_text="Sodium per unit (mg)")
    cholesterol = models.FloatField(default=0, help_text="Cholesterol per unit (mg)")

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(calories__gte=0), name="food_calories_nonneg"),
            models.CheckConstraint(check=models.Q(protein__gte=0), name="food_protein_nonneg"),
            models.CheckConstraint(check=models.Q(carbs__gte=0), name="food_carbs_nonneg"),
            models.CheckConstraint(check=models.Q(fat__gte=0), name="food_fat_nonneg"),
            models.CheckConstraint(check=models.Q(fiber__gte=0), name="food_fiber_nonneg"),
            models.CheckConstraint(check=models.Q(sugar__gte=0), name="food_sugar_nonneg"),
            models.CheckConstraint(check=models.Q(sodium__gte=0), name="food_sodium_nonneg"),
            models.CheckConstraint(
                check=models.Q(cholesterol__gte=0), name="food_cholesterol_nonneg"
            ),
        ]
        indexes = [
            models.Index(fields=["name"], name="food_name_idx"),
        ]

    def __str__(self):
        return self.name


class DiaryEntry(models.Model):
    MEAL_CHOICES = [
        ("breakfast", "Breakfast"),
        ("lunch", "Lunch"),
        ("supper", "Supper"),
        ("dinner", "Dinner"),
        ("snack", "Snack"),
    ]

    date = models.DateField()
    meal_type = models.CharField(max_length=20, choices=MEAL_CHOICES)
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name="entries")
    quantity = models.FloatField(default=1)
    unit = models.CharField(max_length=20, default="g")

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(quantity__gte=0), name="diary_quantity_nonneg"),
        ]
        indexes = [
            models.Index(fields=["date", "meal_type"], name="diary_date_meal_idx"),
        ]

    def __str__(self):
        return f"{self.date} - {self.meal_type} - {self.food.name} ({self.quantity} {self.unit})"


class Goal(models.Model):
    start_date = models.DateField(help_text="Date from which this goal is active")
    calorie_goal = models.FloatField()
    protein_goal = models.FloatField(default=0)
    carb_goal = models.FloatField(default=0)
    fat_goal = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(calorie_goal__gte=0), name="goal_calorie_nonneg"),
            models.CheckConstraint(check=models.Q(protein_goal__gte=0), name="goal_protein_nonneg"),
            models.CheckConstraint(check=models.Q(carb_goal__gte=0), name="goal_carb_nonneg"),
            models.CheckConstraint(check=models.Q(fat_goal__gte=0), name="goal_fat_nonneg"),
        ]
        indexes = [
            models.Index(fields=["start_date"], name="goal_startdate_idx"),
        ]

    def __str__(self):
        return f"Goals from {self.start_date}: {self.calorie_goal} kcal"
