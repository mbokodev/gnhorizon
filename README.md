# Groupe Nouvel Horizon — gnhorizon.ca

Projet Next.js indépendant contenant uniquement GNH et ses médias.

## Développement

```sh
npm ci
npm run dev -- --port 3006
```

Pages : `/`, `/administration`, `/entretien`, `/services-generaux`, `/realisations`, `/a-propos`, `/soumission`.

Le HTML/CSS et les animations sont conservés dans `public/site`. Next.js sert les documents par des réécritures internes, avec des URL propres, sans iframe de navigation. Les cartes Google Maps restent intégrées.

## Docker

```sh
docker build -t gnhorizon .
docker run -d --name gnhorizon --restart unless-stopped -p 3000:3000 gnhorizon
```

Configurer le reverse proxy HTTPS pour `gnhorizon.ca` vers le port 3000 du conteneur. Le certificat TLS et les DNS se configurent chez l’hébergeur.

## État avant publication

- Le formulaire est en mode démonstration : aucune demande n’est envoyée. Brancher un service d’envoi avant l’ouverture au public.
- Les pages restent en `noindex,nofollow` jusqu’à validation de la publication.
- Les photos Unsplash, les polices Google et Google Maps utilisent des services externes.
- Vérifier les garanties commerciales et les témoignages avant publication.

Le dépôt Git local n’a pas encore de remote. Ajouter l’adresse SSH GitHub lorsque disponible.
