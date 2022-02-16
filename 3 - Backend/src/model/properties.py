#!/usr/bin/env python


class Properties(object):
    def __init__(self, created_at, cep, street, neighborhood, city, state, country, number,
                 complement, user, removed, id=None):
        self.id = id
        self.created_at = created_at
        self.cep = cep
        self.street = street
        self.neighborhood = neighborhood
        self.city = city
        self.state = state
        self.country = country
        self.number = number
        self.complement = complement
        self.user = user
        self.removed = removed

    def get_sql_values(self):
        return [self.created_at, self.cep, self.street, self.neighborhood, self.city, self.state, self.country,
                self.number, self.complement, self.user, self.removed]

    def get_values(self):
        return [self.id, self.created_at, self.cep, self.street, self.neighborhood, self.city, self.state,
                self.country, self.number, self.complement, self.user, self.removed]