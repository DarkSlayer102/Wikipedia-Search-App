from flask import Flask, render_template, request
from forms import SearchBar
import wikipedia

app = Flask(__name__)

app.config['SECRET_KEY'] = '123FEDSCD21E3R4FRCEDWS213REFWD'


@app.route('/')
def home():
    my_blog = [
        {
            'name': 'John Adam',
            'age': 20,
            'job': 'no job currently just learning new essential things in programming which help me to get job',
            'Programming_Languages': 'Python,Some Basic of Javascript',
            'Web_Developments': 'Html,css,little web design,Some basics of Javascript'
        }
    ]

    name = 'Name'
    age = 'Age'
    job = 'Job'
    Programming_Language = 'Programming Language'
    Web_Development = 'Web Development'
    return render_template('index.html', my_blog=my_blog, name=name, age=age, job=job, Programming_Language=Programming_Language, Web_Development=Web_Development
                           )


@app.route('/searching', methods=['GET', 'POST'])
def searching():
    form = SearchBar()
    if form.validate_on_submit():
        search_name = form.search.data
        pages = wikipedia.page(search_name)
        page_data = [
            {
                'content': pages.content,
                'link': pages.links,
                'summary': pages.summary,
                'sections': pages.sections,
                'categories': pages.categories
            }
        ]
        searched = wikipedia.search(search_name)
        return render_template('result.html', search_name=search_name, pages=pages, page_data=page_data, searched=searched)
    return render_template('searching.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
