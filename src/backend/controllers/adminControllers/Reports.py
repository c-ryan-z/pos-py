from PyQt6 import QtWidgets as Qtw
from PyQt6.QtCharts import QLineSeries, QChart, QChartView, QValueAxis, QBarCategoryAxis, QScatterSeries, QPieSlice, \
    QPieSeries
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor

from src.backend.controllers.controller_utility import shadow_effect
from src.backend.database.admin.reports import get_monthly_sales, get_weekly_sales, get_daily_sales, get_annual_sales, \
    get_unique_years, get_yearly_sum, get_top_products
from src.frontend.admin.AdminReports import Ui_admin_reports


class Reports(Qtw.QWidget):
    def __init__(self, main_app):
        super().__init__()
        self.ui = Ui_admin_reports()
        self.ui.setupUi(self)
        self.main_app = main_app
        self.chart_view = None

        main_app.mainLoggedIn.connect(self.initialize_report)
        self.ui.cb_linechart.currentIndexChanged.connect(self.update_linechart)
        shadow_effect(self.ui.gb_PieChart)

    def initialize_report(self, user_info):
        if user_info[2] != "admin":
            return

        self.ui.lb_monthly.setText(get_monthly_sales())
        self.ui.lb_weekly.setText(get_weekly_sales())
        self.ui.lb_daily.setText(get_daily_sales())
        self.ui.lb_annual.setText(get_annual_sales())

        years = get_unique_years()
        self.ui.cb_linechart.addItems(years)

        linechart = get_yearly_sum(years[0])
        pie_data = get_top_products()

        self.show_sales_chart(linechart)
        self.top_products(pie_data)

    def show_sales_chart(self, data=None):
        series = QLineSeries()
        scatter = QScatterSeries()

        for point in data:
            series.append(*point)
            scatter.append(*point)

        chart = QChart()
        chart.addSeries(series)
        chart.addSeries(scatter)
        chart.setTitle("Sales Chart")
        chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)

        axisY = QValueAxis()
        axisY.setGridLineVisible(False)
        axisX = QBarCategoryAxis()
        axisX.setGridLineVisible(False)
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]
        axisX.append(months)

        chart.addAxis(axisY, Qt.AlignmentFlag.AlignLeft)
        chart.addAxis(axisX, Qt.AlignmentFlag.AlignBottom)
        series.attachAxis(axisY)
        series.attachAxis(axisX)
        scatter.attachAxis(axisY)
        scatter.attachAxis(axisX)

        if self.chart_view is not None:
            self.ui.layout_linechart.removeWidget(self.chart_view)

        self.chart_view = QChartView(chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)

        self.ui.layout_linechart.addWidget(self.chart_view)

    def update_linechart(self):
        year = self.ui.cb_linechart.currentText()
        if year:
            linechart = get_yearly_sum(year)
            self.show_sales_chart(linechart)

    def top_products(self, data=None):
        series = QPieSeries()

        # Define your colors
        colors = [QColor(173, 216, 230),  # light blue
                  QColor(144, 238, 144),  # light green
                  QColor(255, 165, 0),  # orangy yellow
                  QColor(255, 182, 193),  # light red
                  QColor(75, 0, 130)]  # dark purple

        for i, (product, sales) in enumerate(data):
            pie_element = QPieSlice()
            pie_element.setLabel(product)
            pie_element.setValue(sales)
            pie_element.setColor(colors[i % len(colors)])  # Set color
            series.append(pie_element)

        series.setLabelsPosition(QPieSlice.LabelPosition.LabelOutside)
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Top Products")

        chart.legend().setAlignment(Qt.AlignmentFlag.AlignRight)

        chart_view = QChartView(chart)

        self.ui.layout_piechart.addWidget(chart_view)

    def clear_data(self):
        if self.chart_view is not None:
            self.chart_view.chart().removeAllSeries()
            self.ui.layout_linechart.removeWidget(self.chart_view)
            self.chart_view = None

        self.ui.lb_monthly.clear()
        self.ui.lb_weekly.clear()
        self.ui.lb_daily.clear()
        self.ui.lb_annual.clear()

        self.ui.cb_linechart.clear()

        for i in reversed(range(self.ui.layout_piechart.count())):
            widgetToRemove = self.ui.layout_piechart.itemAt(i).widget()
            self.ui.layout_piechart.removeWidget(widgetToRemove)
            widgetToRemove.setParent(None)
