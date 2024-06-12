def render_restaurante_detail(restaurante):
    return {
        'id': restaurante.id,
        'name': restaurante.name,
        'address': restaurante.address,
        'city': restaurante.city,
        'phone': restaurante.phone,
        'description': restaurante.description,
        'rating': restaurante.rating,
    }

def render_restaurante_list(restaurantes):
    return [
        {
            'id': restaurante.id,
            'name': restaurante.name,
            'address': restaurante.address,
            'city': restaurante.city,
            'phone': restaurante.phone,
            'description': restaurante.description,
            'rating': restaurante.rating,
        }
        for restaurante in restaurantes
    ]