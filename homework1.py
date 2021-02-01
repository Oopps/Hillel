

def parse(query: str) -> dict:
    new_dict = {}
    if '?' not in query:
        return new_dict
    else:
        params = query.split('?')
        query = params[1]
        params = query.split('&')
        for i in params:
            if i != '':
                item = i.split('=')
                new_dict[item[0]] = item[1]
        return new_dict


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('http://example.com/?name=Dima&age=28') == {'name': 'Dima', 'age': '28'}
    assert parse('https://mail.google.com/mail/u/0/#inbox/FMfcgxwKjxBkvzkhSlzNbDFjHmBJfSnJ') == {}
    assert parse('https://') == {}
    assert parse('http://example.com/?name=Dima&age=28&birthday=06.08.1979') == {'name': 'Dima', 'age': '28',
                                                                                 'birthday': '06.08.1979'}
    assert parse('http://example.com/?name=Dima&age=28&birthday=06.08.1979&') == {'name': 'Dima', 'age': '28',
                                                                                 'birthday': '06.08.1979'}


def parse_cookie(query: str) -> dict:
    new_dict = {}
    params = query.split(';')
    for i in params:
        if i != '':
            item = i.split('=')
            if len(item) > 2:
                new_item = [item[0], item[1]]
                new_dict[new_item[0]] = '='.join(item[1:])
            elif len(item) == 1:
                new_dict[item[0]] = 'Empty!!!'
            else:
                new_dict[item[0]] = item[1]
    return new_dict


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=User;age=28;birthday=06.08.1979') == {'name': 'User', 'age': '28',
                                                                    'birthday': '06.08.1979'}
    assert parse_cookie('name=User;age=28;email=mail@mail.com') == {'name': 'User', 'age': '28',
                                                                    'email': 'mail@mail.com'}
    assert parse_cookie('name=Dima=User=test;age=28;') == {'name': 'Dima=User=test', 'age': '28'}
    assert parse_cookie('name;age=28;') == {'name': 'Empty!!!', 'age': '28'}
    assert parse_cookie('name;age') == {'name': 'Empty!!!', 'age': 'Empty!!!'}
