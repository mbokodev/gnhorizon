# SEO — gnhorizon.ca

Les sept pages publiques sont indexables et possèdent une URL canonique unique, un titre et une description spécifiques, des métadonnées Open Graph/Twitter et un visuel de partage local de 1200 × 630 pixels.

Les données structurées JSON-LD décrivent l’organisation, son site, les pages et les trois domaines de service. Elles n’incluent ni notes, ni avis, ni horaires ou adresse de rue non confirmés.

- Sitemap : https://gnhorizon.ca/sitemap.xml
- Robots : https://gnhorizon.ca/robots.txt
- Les anciennes URL HTML redirigent en 308 vers les URL canoniques.
- Les paramètres de soumission ne créent pas de nouvelles URL canoniques.

## Validation locale

```sh
npm run build
npm run start -- --port 3007
python3 scripts/check-seo.py http://localhost:3007
```

## Après déploiement

1. Ajouter la propriété de domaine `gnhorizon.ca` à Google Search Console et valider le DNS avec la valeur TXT fournie par Google.
2. Soumettre `https://gnhorizon.ca/sitemap.xml`, puis inspecter la page d’accueil et les pages de services.
3. Tester le JSON-LD avec le test des résultats enrichis de Google.
4. Compléter la fiche Google Business Profile avec les informations exactes de l’entreprise et les zones réellement desservies.
5. Remplacer les témoignages et les exemples de réalisations par des références vérifiables et brancher le formulaire avant de chercher à augmenter les demandes.

L’indexation et les positions ne sont pas garanties par ces réglages. Les contenus locaux utiles, la réputation et les références de l’entreprise restent à développer.
