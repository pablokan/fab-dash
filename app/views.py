from flask_appbuilder import BaseView, expose, has_access
from flask import redirect, url_for
from . import appbuilder

# ============= bokeh
from bokeh.plotting import figure, output_file, show, save
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
output_file("app/templates/lineas.html")
p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
p.line(x, y, legend_label="Temp.", line_width=2)
p.hbar()
save(p)
# ============= bokeh



class MyView(BaseView):

    default_view = "method3"

    @expose("/method7/<string:param1>")
    @has_access
    def method7(self, param1):
        param1 = f"Hi {param1}"
        return param1


    @expose("/method6/")
    @has_access
    def method6(self):
        ruta = '<script>window.open("http://0.0.0.0:8085/app/templates/continentsCallBack.py", "MyWindow", "height=640,width=960,menubar=no,scrollbars=no,location=no,status=no");</script>'
        redi = '<script>window.location.href = "http://0.0.0.0:8085/myview/method4/bokeh";</script>'
        rutaMASredi = ruta + redi
        return rutaMASredi



    @expose("/method5/<string:param1>")
    @has_access
    def method5(self, param1):
        param1 = f"Hi {param1}"
        return param1

    @expose("/method3/")
    @has_access
    def method3(self):
        return self.render_template("method3.html")

    @expose("/method4/<string:param1>")
    @has_access
    def method4(self, param1):
        a = open("app/templates/lineas.html", "r")
        aF = a.read()
        if aF[0] != "{":
            aF = '{% extends "appbuilder/base.html" %}  {% block content %}' + aF + '{% endblock %}'
            a.close()
            a = open("app/templates/lineas.html", "w")
            a.write(aF)
        a.close()
        return self.render_template("lineas.html", param1=param1)



appbuilder.add_view(MyView, "Method3", href="/myview/method3", category="My View")
# Use add link instead there is no need to create MyView twice.
appbuilder.add_link("Method4", href="/myview/method4/bokeh", category="My View")
appbuilder.add_link("Method5", href="/myview/method5/kan", category="My View")
appbuilder.add_link("Method6", href="/myview/method6", category="Pafuera")
appbuilder.add_link("Method7", href="/myview/method7/kan", category="Pafuera")
appbuilder.add_link("Google", href="https://www.google.com", category="Google")

