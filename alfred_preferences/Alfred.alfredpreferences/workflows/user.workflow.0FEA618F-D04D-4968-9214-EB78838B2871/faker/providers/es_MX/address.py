# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from ..address import Provider as AddressProvider
#import locale

class Provider(AddressProvider):
    #current_locale = locale.setlocale(locale.LC_ALL, "es_MX.UTF-8")
    city_prefixes = ('Sur', 'Norte',)
    city_adjetives = ('Nueva', 'Vieja',)
    city_suffixies = ('de la Montaña', 'los bajos', 'los altos', )
    street_prefixes = (
        'Ampliación', 'Andador', 'Avenida', 'Boulevard', 'Calle', 'Callejón',
        'Calzada', 'Cerrada', 'Circuito', 'Circunvalación', 'Continuación',
        'Corredor', 'Diagonal', 'Eje vial', 'Pasaje', 'Peatonal', 'Periférico',
        'Privada', 'Prolongación', 'Retorno', 'Viaducto'
        )
    building_number_formats = ('#####', '####', '###')
    postcode_formats = ('#####', '#####-####')
    ## States and abbrs from Mexico from INEGI
    ## http://www.inegi.org.mx/geo/contenidos/geoestadistica/CatalogoClaves.aspx
    states = (
        ('AGS','Aguascalientes'), ('BC','Baja California'),
        ('BCS','Baja California Sur'), ('CAMP','Campeche'),
        ('COAH', 'Coahuila de Zaragoza'), ('COL', 'Colima'),
        ('CHIS', 'Chiapas'), ('CHIH', 'Chihuahua'),
        ('DF','Distrito Federal'), ('DGO', 'Durango'),
        ('GTO', 'Guanajuato'), ('GRO', 'Guerrero'), ('HGO', 'Hidalgo'),
        ('JAL', 'Jalisco'), ('MEX', 'México'),
        ('MICH', 'Michoacán de Ocampo'), ('MOR', 'Morelos'),
        ('NAY', 'Nayarit'), ('NL', 'Nuevo León'), ('OAX', 'Oaxaca'),
        ('PUE','Puebla'), ('QRO', 'Querétaro'),
        ('Q. ROO', 'Quintana Roo'), ('SLP', 'San Luis Potosí'),
        ('SIN', 'Sinaloa'), ('SON', 'Sonora'), ('TAB', 'Tabasco'),
        ('TAMPS','Tamaulipas'), ('TLAX','Tlaxcala'),
        ('VER', 'Veracruz de Ignacio de la Llave'),
        ('YUC', 'Yucatán'), ('ZAC','Zacatecas'),)

    zip_codes = {
        ## The ZipCodes has a begin & final range
        ## Source: Norma Técnica de Domicilios INEGI
        'AGS': (20000, 20999), 'BC' : (21000, 22999),
        'BCS': (23000, 23999), 'CAMP' : (24000, 24999),
        'COAH': (25000, 27999), 'COL': (28000, 28999),
        'CHIS': (29000, 30999), 'CHIH': (31000, 33999),
        'DF': (1000, 19999), 'DGO': (36000, 35999),
        'GTO': (36000, 38999), 'GRO': (39000, 41999),
        'HGO': (42000, 43999), 'JAL': (44000, 49999),
        'MEX': (50000, 57999), 'MICH': (58000, 61999),
        'MOR': (62000, 62999), 'NAY': (63000, 63999),
        'NL': (64000, 67999), 'OAX': (68000, 71999),
        'PUE': (72000, 75999), 'QRO': (76000, 76999),
        'Q. ROO': (77000, 75999), 'SLP': (78000, 79999),
        'SIN': (80000, 82999), 'SON': (83000, 85999),
        'TAB': (86000, 86999), 'TAMPS': (87000, 89999),
        'TLAX': (90000, 90999), 'VER': (91000, 97999),
        'YUC': (97000, 97999), 'ZAC': (98000, 99999)
    }
    ## List of Countries https://www.un.org/es/members/
    countries = (
        'Afganistán', 'Albania', 'Alemania', 'Andorra', 'Angola',
        'Antigua y Barbuda', 'Arabia Saudita', 'Argelia', 'Argentina',
        'Armenia', 'Australia', 'Austria', 'Azerbaiyán',
        'Bahamas', 'Bahrein', 'Bangladesh', 'Barbados', 'Belarús',
        'Bélgica', 'Belice', 'Benin', 'Bhután', 'Bolivia',
        'Bosnia y Herzegovina', 'Botswana', 'Brasil', 'Brunei Darussalam',
        'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Camboya',
        'Camerún', 'Canadá', 'Chad', 'Chile', 'China', 'Chipre','Colombia',
        'Comoras', 'Congo', 'Costa Rica', 'Côte d\'Ivoire', 'Croacia',
        'Cuba', 'Dinamarca', 'Djibouti', 'Dominicana', 'Ecuador', 'Egipto',
        'El Salvador', 'Emiratos Árabes Unidos', 'Eritrea', 'Eslovaquia',
        'Eslovenia', 'España', 'Estados Unidos de América', 'Estonia',
        'Etiopía', 'ex República Yugoslava de Macedonia',
        'Federación de Rusia', 'Fiji', 'Filipinas', 'Finlandia', 'Francia',
        'Gabón', 'Gambia', 'Georgia', 'Ghana', 'Granada', 'Grecia',
        'Guatemala', 'Guinea', 'Guinea Bissau', 'Guinea Ecuatorial',
        'Guyana', 'Haití', 'Honduras', 'Hungría', 'India', 'Indonesia',
        'Irán', 'Iraq', 'Irlanda', 'Islandia', 'Islas Marshall',
        'Islas Salomón', 'Israel', 'Italia', 'Jamaica', 'Japón',
        'Jordania', 'Kazajstán', 'Kenya', 'Kirguistán', 'Kiribati',
        'Kuwait', 'Lesotho', 'Letonia', 'Líbano', 'Liberia', 'Libia',
        'Liechtenstein', 'Lituania', 'Luxemburgo', 'Madagascar',
        'Malasia', 'Malawi', 'Maldivas', 'Mali', 'Malta','Marruecos',
        'Mauricio', 'Mauritania', 'México', 'Micronesia', 'Mónaco',
        'Mongolia', 'Montenegro','Mozambique','Myanmar', 'Namibia',
        'Nauru', 'Nicaragua', 'Niger', 'Nigeria', 'Noruega',
        'Nueva Zelandia', 'Omán', 'Países Bajos', 'Pakistán', 'Palau',
        'Panamá', 'Papua Nueva Guinea', 'Paraguay', 'Perú', 'Polonia',
        'Portugal', 'Qatar',
        'Reino Unido de Gran Bretaña e Irlanda del Norte',
        'República Árabe Siria', 'República Centroafricana',
        'República Checa', 'República de Corea', 'República de Moldova',
        'República Democrática del Congo',
        'República Democrática Popular Lao',
        'República Dominicana',
        'República Federal Democrática de Nepal',
        'República Popular Democrática de Corea',
        'República Unida de Tanzanía', 'Rumania', 'Rwanda',
        'Saint Kitts y Nevis', 'Samoa', 'San Marino', 'Santa Lucía',
        'Santo Tomé y Príncipe', 'San Vicente y las Granadinas',
        'Senegal', 'Serbia', 'Seychelles', 'Sierra Leona', 'Singapur',
        'Somalia', 'Sri Lanka', 'Sudáfrica', 'Sudán', 'Sudán del Sur',
        'Suecia', 'Suiza', 'Suriname', 'Swazilandia', 'Tailandia',
        'Tayikistán', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad y Tabago',
        'Túnez', 'Turkmenistán', 'Turquía', 'Tuvalu', 'Ucrania', 'Uganda',
        'Uruguay', 'Uzbekistán', 'Vanuatu', 'Venezuela', 'Vietman',
        'Yemen', 'Zambia', 'Zimbabwe'
    )

    city_formats = (
        '{{city_adjetive}} {{country}}',
        'San {{first_name}} {{city_suffix}}',
    )
    street_name_formats = (
        '{{street_prefix}} {{last_name}}',
        '{{street_prefix}} {{country}}',
        '{{street_prefix}} {{state}}',
        '{{street_prefix}} {{city_prefix}} {{last_name}}'
    )
    street_address_formats = (
        #'{{building_number}} {{street_name}}',
        '{{street_name}} {{secondary_address}}',
        #'{{building_number}} {{street_name}} {{secondary_address}}',
    )
    address_formats = (
        "{{street_address}}\n{{city}}, {{state_abbr}} {{postcode}}",
    )
    secondary_address_formats = ('### ###', '### Interior ###',
        '### Edif. ### , Depto. ###')

    @classmethod
    def city_prefix(cls):
        return cls.random_element(cls.city_prefixes)

    @classmethod
    def city_suffix(cls):
        return cls.random_element(cls.city_suffixies)

    @classmethod
    def city_adjetive(cls):
        return cls.random_element(cls.city_adjetives)

    @classmethod
    def street_prefix(cls):
        """
        :example 'Avenida'
        """
        return cls.random_element(cls.street_prefixes)
    @classmethod
    def secondary_address(cls):
        """
        :example '020 Interior 999'
        """
        return cls.numerify(cls.random_element(cls.secondary_address_formats))

    @classmethod
    def state(cls):
        """
        example: u'Guerrero'
        """
        return cls.random_element(cls.states)[1]

    @classmethod
    def state_abbr(cls):
        """
        example: u'GRO'
        """
        return cls.random_element(cls.states)[0]

