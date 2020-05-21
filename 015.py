#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
persons = ['John', 'Marissa','Pete', 'Dayton']

for person in persons:
	for other_persons in persons:
		if person == other_persons:
			pass
		else:
			print(person + ' meets ' + other_persons)