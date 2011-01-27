# coding: utf8

def create():

    form = crud.create(person)
    form_favs = crud.create(favorite_music)
    persons = db().select(db.person.ALL, db.favorite_music.ALL, left=favorite_music.on(person.id == favorite_music.person))

    return dict(form = form, form_favs = form_favs, persons = persons)
    

def simple_report():

    form = plugin_appreport.REPORTFORM(table=person)

    if form.accepts(request.vars, session):
        return plugin_appreport.REPORT(table = person, title = 'List of persons', filter = dict(form.vars))

    return dict(form = form)
    
def report_persons():

    return dict(persons = db(person.id > 0).select())


def complex_report():

    form = plugin_appreport.REPORTFORM(table=person)

    if form.accepts(request.vars, session):
        persons = db(form.prep_filter(filter = dict(form.vars))).select()
        html = response.render('person/report_persons.html', dict(persons = persons))
        return plugin_appreport.REPORT(html = html)

    return dict(form = form)



def custom_report():
    
    html = """<html>
                <head>
                    <meta charset="utf-8" />
                </head>
                <body>
                    <h2>Report of persons</h2>
                    <table>
                        <thead>
                            <tr>
                                <th>Author</th>
                                <th>Email</th>
                                <th>Twitter</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Lucas D'Avila</td>
                                <td>lucassdvl@gmail.com</td>
                                <td>@lucadavila</td>                                
                            </tr>
                        </tbody>
                    </table>
                </body>
            </html>
    """
    return plugin_appreport.REPORT(html = html, title = 'my custom report using the plugin appreport')
