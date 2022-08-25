from flask import Flask, render_template, request


app = Flask(__name__, static_folder='static')

@app.route('/cadbury')
def dynamic():
    return render_template('index.html')



# /api/v1/brand?name=nestle
@app.route('/api/v1/brand')
def main():
    brandname = request.args['name']
    return {
        'brand_name': 'Cadbury',
        'bio': ' Inspiring and investing into a world of chocolate lovers for  200 years ❤️',
        'profile_icon': 'https://www.ladbible.com/cdn-cgi/image/width=648,quality=70,format=jpeg,fit=pad,dpr=1/https%3A%2F%2Fs3-images.ladbible.com%2Fs3%2Fcontent%2F137e41675ea9f03a075509b6c0b7dd7f.jpg',
        'banner_url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSDrnyjH_j8C5fsEq_dC_qp1GN-ps9jy4yPte3VanD8FERZMMpR6FKGr2if6gbK4mqTSfI&usqp=CAU'
    }


@app.route('/api/v1/links')
def links():
    brandname = request.args['name']
    return {
        'social_links': [
            {
                'url': 'https://www.instagram.com/cadburydairymilkin',
                'platform': 'instagram'
            },
            {
                'url': 'https://www.facebook.com/cadburyperk/',
                'platform': 'Facebook'
            },
            {
                'url': 'https://twitter.com/cadburyperk_ind',
                'platform': 'Twitter'
            }
        ],
        'links': [
            {
                'url': 'https://www.cadbury.co.uk/',
                'text': 'Website'
            },
            {
                'url': 'https://www.cadbury.co.uk/',
                'text': 'Charity'
            },
            {
                'url': 'https://www.cadbury.co.uk/',
                'text': 'FeedBack'
            },
            {
                'url': 'https://www.cadbury.co.uk/',
                'text': 'Community Forum'
            }
        ]
    }


@app.route('/api/v1/posts')
def posts():
    return {
        'posts': [
            {
                'title': 'Sweet Sweet Holidays',
                'thumbnail': 'https://www.ladbible.com/cdn-cgi/image/width=648,quality=70,format=jpeg,fit=pad,dpr=1/https%3A%2F%2Fs3-images.ladbible.com%2Fs3%2Fcontent%2F137e41675ea9f03a075509b6c0b7dd7f.jpg'
            },
            {
                'title': 'Manking a difference',
                'thumbnail': 'https://www.ladbible.com/cdn-cgi/image/width=648,quality=70,format=jpeg,fit=pad,dpr=1/https%3A%2F%2Fs3-images.ladbible.com%2Fs3%2Fcontent%2F137e41675ea9f03a075509b6c0b7dd7f.jpg'
            },
            {
                'title': 'We are hiring!',
                'thumbnail': 'https://www.ladbible.com/cdn-cgi/image/width=648,quality=70,format=jpeg,fit=pad,dpr=1/https%3A%2F%2Fs3-images.ladbible.com%2Fs3%2Fcontent%2F137e41675ea9f03a075509b6c0b7dd7f.jpg'
            }
        ]
    }

app.run(debug=True)