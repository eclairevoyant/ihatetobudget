import datetime

from ..models import Expense


def sheet_date_list(request):
    #  XXX: `request.user.is_authenticated` should be enough, since all expenses
    # are available to any user.
    return (
        {"sheet_date_list": Expense.objects.dates("date", "month")}
        if request.user.is_authenticated
        else {}
    )


def current_sheet_date(request):
    now = datetime.datetime.now()
    for sheet_date in sheet_date_list(request).get("sheet_date_list", []):
        if sheet_date.month == now.month and sheet_date.year == now.year:
            return {"current_sheet_date": sheet_date}
    return {}
