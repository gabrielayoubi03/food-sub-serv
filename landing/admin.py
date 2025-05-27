from django.contrib import admin
from .models import Restaurant, Customer, Transaction, Reward

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'points_multiplier')
    search_fields = ('name', 'email')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'total_points')
    search_fields = ('user__first_name', 'user__last_name', 'phone')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('customer', 'restaurant', 'amount', 'points_earned', 'created_at')
    list_filter = ('restaurant', 'created_at')

@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'points_required', 'is_active')
    list_filter = ('restaurant', 'is_active')
