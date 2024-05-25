from django.contrib import admin

from portfolio_app.models import Event, Exchange, Portfolio, Transaction, PortfolioItem

@admin.action(description="notified True")
def notifiedTrue(model_admin, request, queryset):
    queryset.update(notified=True)

@admin.action(description="notified False")
def notifiedFalse(model_admin, request, queryset):
    queryset.update(notified=False)

admin.site.register(Event)

admin.site.register(Exchange)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    model = Portfolio

    list_display_links = (
        'name',
        'balance',
        'profit',
        'percent', )

    list_display = (
        'name',
        'balance',
        'profit',
        'percent', )

class TransactionInLine(admin.StackedInline):
    model = Transaction
    list_display = ('amount', )
    extra = 1

    @staticmethod
    def amount(obj):
        return obj.amount

@admin.register(PortfolioItem)
class PortfolioItemMainAdmin(admin.ModelAdmin):
    model = PortfolioItem
    inlines = [TransactionInLine, ]
    list_display = (
        'coin_name',
        'profit',
        'percent',)

    list_filter = [
        'portfolio',
        'exchange',]

    actions = [
        notifiedTrue,
        notifiedFalse,]