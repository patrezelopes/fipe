from app.services.parallelum.proxy import Parallelum


def test_get_brands():
    # partial_result = [{'codigo': '1', 'nome': 'Acura'}, {'codigo': '2', 'nome': 'Agrale'}]
    result = Parallelum().get_brands()
    assert result[0].get('codigo')
    assert result[1].get('nome')
