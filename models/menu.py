# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(IMG(_src=URL('static', 'images/iiits_logo.jpg'),_height="55px"),_href="http://www.iiits.ac.in/",_id="web2py-logo")
response.title = T('Feeling hungry?')
response.subtitle ='Welcome to Mess Portal'

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Menu Details'), False, URL('default', 'mess_menu'), []),
    (T('Reserve/Cancel Meal'), False, URL('default', 'reserve_cancel'), [
            (T('Reserve Meal'), False, URL('default', 'reserve_meal'), []),
            (T('Cancel Meal'), False, URL('default', 'cancel_meal'), [])]),
    (T('People'), False, URL('default', 'mess_people'), [
            (T('Mess-Incharge'), False, URL('default', 'mess_incharge')),
              (T('Caterers'), False, URL('default', 'mess_caterer'))])]

response.managing_admin=[
    (T('Add/Change/Remove'), False, URL('default', 'index'), [
            (T('People'), False, URL('default', 'admin_change_remove.html?modify=People'), []),
            (T('Caterer'), False, URL('default', 'admin_change_remove.html?modify=Caterer'), []),
            (T('Mess Place'), False, URL('default', 'admin_change_remove.html?modify=Mess_Place'), [])]),
    (T('Issue Notifications'), False, URL('default', 'index'), []),
    (T('Approve Registration'), False, URL('default', 'index'), [
            (T('Student'), False, URL('default', 'index'), []),
            (T('Faculty'), False, URL('default', 'index'), []),
            (T('Staff Members'), False, URL('default', 'index'), []),
            (T('Mess Committee Member'), False, URL('default', 'index'), []),
            (T('Caterer'), False, URL('default', 'index'), [])]),
    (T('Change Mess Menu'), False, URL('default', 'index'), [])]

response.caterer=[
    (T('Number of people'), False, URL('default', 'caterer_people'), []),]

if auth.is_logged_in():
    if auth.user.account_class!='Admin':
        response.menu=response.menu+[
        (T('Complaint Section'), False, URL('default', 'complaint_section'), [])]
    else:
        response.menu=response.menu+[
        (T('Switch to Admin Mode'), False, URL('default_admin','index'), [])]


if "auth" in locals(): auth.wikimenu()
