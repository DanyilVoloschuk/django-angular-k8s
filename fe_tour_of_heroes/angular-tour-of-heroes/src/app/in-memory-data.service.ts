import { Injectable } from '@angular/core';
import { InMemoryDbService } from 'angular-in-memory-web-api';
import { Hero } from './hero';

@Injectable({
  providedIn: 'root',
})
export class InMemoryDataService implements InMemoryDbService {
  createDb() {
    const heroes = [
      { id: 12, firstname: 'Dr. Nice' },
      { id: 13, firstname: 'Bombasto' },
      { id: 14, firstname: 'Celeritas' },
      { id: 15, firstname: 'Magneta' },
      { id: 16, firstname: 'RubberMan' },
      { id: 17, firstname: 'Dynama' },
      { id: 18, firstname: 'Dr. IQ' },
      { id: 19, firstname: 'Magma' },
      { id: 20, firstname: 'Tornado' }
    ];
    return {heroes};
  }

  // Overrides the genId method to ensure that a hero always has an id.
  // If the heroes array is empty,
  // the method below returns the initial number (11).
  // if the heroes array is not empty, the method below returns the highest
  // hero id + 1.
  genId(heroes: Hero[]): number {
    return heroes.length > 0 ? Math.max(...heroes.map(hero => hero.id)) + 1 : 11;
  }
}
