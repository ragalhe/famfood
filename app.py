"""
🍽️ FamFood - Planificador de Menú Semanal Familiar
Multi-idioma: ES, EN, FR, DE
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import json
import random

# =====================================================
# CONFIGURACIÓN DE PÁGINA
# =====================================================

st.set_page_config(
    page_title="FamFood - Menu Planner",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# TRADUCCIONES
# =====================================================

TRANSLATIONS = {
    'es': {
        'app_name': 'FamFood',
        'tagline': 'Planifica las comidas de tu familia',
        'weekly_menu': '📅 Menú Semanal',
        'recipes': '🍳 Recetas',
        'shopping_list': '🛒 Lista de Compra',
        'family': '👨‍👩‍👧‍👦 Mi Familia',
        'settings': '⚙️ Ajustes',
        'language': 'Idioma',
        'week_of': 'Semana del',
        'lunch': 'Comida',
        'dinner': 'Cena',
        'monday': 'Lunes',
        'tuesday': 'Martes',
        'wednesday': 'Miércoles',
        'thursday': 'Jueves',
        'friday': 'Viernes',
        'saturday': 'Sábado',
        'sunday': 'Domingo',
        'generate_menu': '🎲 Generar menú automático',
        'clear_menu': '🗑️ Limpiar menú',
        'generate_list': '📝 Generar lista de compra',
        'share_whatsapp': '📤 Compartir por WhatsApp',
        'people': 'Personas',
        'budget': 'Presupuesto semanal',
        'allergies': 'Alergias',
        'preferences': 'Preferencias',
        'no_pork': 'Sin cerdo',
        'no_spicy': 'Sin picante',
        'vegetarian': 'Vegetariano',
        'quick_meals': 'Comidas rápidas (<30 min)',
        'save': 'Guardar',
        'search_recipe': 'Buscar receta...',
        'all_categories': 'Todas las categorías',
        'meat': '🥩 Carnes',
        'fish': '🐟 Pescados',
        'vegetables': '🥬 Verduras',
        'pasta': '🍝 Pastas',
        'soups': '🍲 Sopas',
        'quick': '⚡ Rápidas',
        'kids': '👶 Para niños',
        'prep_time': 'Tiempo',
        'servings': 'Raciones',
        'difficulty': 'Dificultad',
        'easy': 'Fácil',
        'medium': 'Media',
        'hard': 'Difícil',
        'ingredients': 'Ingredientes',
        'instructions': 'Preparación',
        'add_to_menu': '➕ Añadir al menú',
        'fruits': '🍎 Frutas',
        'dairy': '🧀 Lácteos',
        'bakery': '🍞 Panadería',
        'frozen': '🧊 Congelados',
        'others': '📦 Otros',
        'estimated_cost': 'Coste estimado',
        'item_bought': 'Marcar comprado',
        'premium_title': '⭐ FamFood Premium',
        'premium_desc': 'Desbloquea +500 recetas, sugerencias IA y más',
        'premium_price': '3,99€/mes',
        'try_free': 'Probar 7 días gratis',
        'nuts': 'Frutos secos',
        'gluten': 'Gluten',
        'lactose': 'Lactosa',
        'eggs': 'Huevos',
        'shellfish': 'Mariscos',
        'none': 'Ninguna',
        'min': 'min',
        'welcome': '¡Bienvenido a FamFood!',
        'welcome_text': 'Planifica las comidas de tu familia de forma fácil y ahorra tiempo y dinero.',
    },
    'en': {
        'app_name': 'FamFood',
        'tagline': 'Plan your family meals',
        'weekly_menu': '📅 Weekly Menu',
        'recipes': '🍳 Recipes',
        'shopping_list': '🛒 Shopping List',
        'family': '👨‍👩‍👧‍👦 My Family',
        'settings': '⚙️ Settings',
        'language': 'Language',
        'week_of': 'Week of',
        'lunch': 'Lunch',
        'dinner': 'Dinner',
        'monday': 'Monday',
        'tuesday': 'Tuesday',
        'wednesday': 'Wednesday',
        'thursday': 'Thursday',
        'friday': 'Friday',
        'saturday': 'Saturday',
        'sunday': 'Sunday',
        'generate_menu': '🎲 Generate automatic menu',
        'clear_menu': '🗑️ Clear menu',
        'generate_list': '📝 Generate shopping list',
        'share_whatsapp': '📤 Share via WhatsApp',
        'people': 'People',
        'budget': 'Weekly budget',
        'allergies': 'Allergies',
        'preferences': 'Preferences',
        'no_pork': 'No pork',
        'no_spicy': 'No spicy',
        'vegetarian': 'Vegetarian',
        'quick_meals': 'Quick meals (<30 min)',
        'save': 'Save',
        'search_recipe': 'Search recipe...',
        'all_categories': 'All categories',
        'meat': '🥩 Meat',
        'fish': '🐟 Fish',
        'vegetables': '🥬 Vegetables',
        'pasta': '🍝 Pasta',
        'soups': '🍲 Soups',
        'quick': '⚡ Quick',
        'kids': '👶 For kids',
        'prep_time': 'Time',
        'servings': 'Servings',
        'difficulty': 'Difficulty',
        'easy': 'Easy',
        'medium': 'Medium',
        'hard': 'Hard',
        'ingredients': 'Ingredients',
        'instructions': 'Instructions',
        'add_to_menu': '➕ Add to menu',
        'fruits': '🍎 Fruits',
        'dairy': '🧀 Dairy',
        'bakery': '🍞 Bakery',
        'frozen': '🧊 Frozen',
        'others': '📦 Others',
        'estimated_cost': 'Estimated cost',
        'item_bought': 'Mark as bought',
        'premium_title': '⭐ FamFood Premium',
        'premium_desc': 'Unlock +500 recipes, AI suggestions and more',
        'premium_price': '€3.99/month',
        'try_free': 'Try 7 days free',
        'nuts': 'Nuts',
        'gluten': 'Gluten',
        'lactose': 'Lactose',
        'eggs': 'Eggs',
        'shellfish': 'Shellfish',
        'none': 'None',
        'min': 'min',
        'welcome': 'Welcome to FamFood!',
        'welcome_text': 'Plan your family meals easily and save time and money.',
    },
    'fr': {
        'app_name': 'FamFood',
        'tagline': 'Planifiez les repas de votre famille',
        'weekly_menu': '📅 Menu Hebdomadaire',
        'recipes': '🍳 Recettes',
        'shopping_list': '🛒 Liste de Courses',
        'family': '👨‍👩‍👧‍👦 Ma Famille',
        'settings': '⚙️ Paramètres',
        'language': 'Langue',
        'week_of': 'Semaine du',
        'lunch': 'Déjeuner',
        'dinner': 'Dîner',
        'monday': 'Lundi',
        'tuesday': 'Mardi',
        'wednesday': 'Mercredi',
        'thursday': 'Jeudi',
        'friday': 'Vendredi',
        'saturday': 'Samedi',
        'sunday': 'Dimanche',
        'generate_menu': '🎲 Générer menu automatique',
        'clear_menu': '🗑️ Effacer le menu',
        'generate_list': '📝 Générer liste de courses',
        'share_whatsapp': '📤 Partager par WhatsApp',
        'people': 'Personnes',
        'budget': 'Budget hebdomadaire',
        'allergies': 'Allergies',
        'preferences': 'Préférences',
        'no_pork': 'Sans porc',
        'no_spicy': 'Sans épices',
        'vegetarian': 'Végétarien',
        'quick_meals': 'Repas rapides (<30 min)',
        'save': 'Enregistrer',
        'search_recipe': 'Rechercher recette...',
        'all_categories': 'Toutes les catégories',
        'meat': '🥩 Viandes',
        'fish': '🐟 Poissons',
        'vegetables': '🥬 Légumes',
        'pasta': '🍝 Pâtes',
        'soups': '🍲 Soupes',
        'quick': '⚡ Rapides',
        'kids': '👶 Pour enfants',
        'prep_time': 'Temps',
        'servings': 'Portions',
        'difficulty': 'Difficulté',
        'easy': 'Facile',
        'medium': 'Moyen',
        'hard': 'Difficile',
        'ingredients': 'Ingrédients',
        'instructions': 'Préparation',
        'add_to_menu': '➕ Ajouter au menu',
        'fruits': '🍎 Fruits',
        'dairy': '🧀 Produits laitiers',
        'bakery': '🍞 Boulangerie',
        'frozen': '🧊 Surgelés',
        'others': '📦 Autres',
        'estimated_cost': 'Coût estimé',
        'item_bought': 'Marquer acheté',
        'premium_title': '⭐ FamFood Premium',
        'premium_desc': 'Débloquez +500 recettes, suggestions IA et plus',
        'premium_price': '3,99€/mois',
        'try_free': 'Essayer 7 jours gratuit',
        'nuts': 'Fruits à coque',
        'gluten': 'Gluten',
        'lactose': 'Lactose',
        'eggs': 'Œufs',
        'shellfish': 'Fruits de mer',
        'none': 'Aucune',
        'min': 'min',
        'welcome': 'Bienvenue sur FamFood!',
        'welcome_text': 'Planifiez facilement les repas de votre famille et économisez temps et argent.',
    },
    'de': {
        'app_name': 'FamFood',
        'tagline': 'Planen Sie die Mahlzeiten Ihrer Familie',
        'weekly_menu': '📅 Wochenmenü',
        'recipes': '🍳 Rezepte',
        'shopping_list': '🛒 Einkaufsliste',
        'family': '👨‍👩‍👧‍👦 Meine Familie',
        'settings': '⚙️ Einstellungen',
        'language': 'Sprache',
        'week_of': 'Woche vom',
        'lunch': 'Mittagessen',
        'dinner': 'Abendessen',
        'monday': 'Montag',
        'tuesday': 'Dienstag',
        'wednesday': 'Mittwoch',
        'thursday': 'Donnerstag',
        'friday': 'Freitag',
        'saturday': 'Samstag',
        'sunday': 'Sonntag',
        'generate_menu': '🎲 Automatisches Menü erstellen',
        'clear_menu': '🗑️ Menü löschen',
        'generate_list': '📝 Einkaufsliste erstellen',
        'share_whatsapp': '📤 Per WhatsApp teilen',
        'people': 'Personen',
        'budget': 'Wochenbudget',
        'allergies': 'Allergien',
        'preferences': 'Präferenzen',
        'no_pork': 'Kein Schweinefleisch',
        'no_spicy': 'Nicht scharf',
        'vegetarian': 'Vegetarisch',
        'quick_meals': 'Schnelle Gerichte (<30 min)',
        'save': 'Speichern',
        'search_recipe': 'Rezept suchen...',
        'all_categories': 'Alle Kategorien',
        'meat': '🥩 Fleisch',
        'fish': '🐟 Fisch',
        'vegetables': '🥬 Gemüse',
        'pasta': '🍝 Pasta',
        'soups': '🍲 Suppen',
        'quick': '⚡ Schnell',
        'kids': '👶 Für Kinder',
        'prep_time': 'Zeit',
        'servings': 'Portionen',
        'difficulty': 'Schwierigkeit',
        'easy': 'Einfach',
        'medium': 'Mittel',
        'hard': 'Schwer',
        'ingredients': 'Zutaten',
        'instructions': 'Zubereitung',
        'add_to_menu': '➕ Zum Menü hinzufügen',
        'fruits': '🍎 Obst',
        'dairy': '🧀 Milchprodukte',
        'bakery': '🍞 Bäckerei',
        'frozen': '🧊 Tiefkühl',
        'others': '📦 Sonstiges',
        'estimated_cost': 'Geschätzte Kosten',
        'item_bought': 'Als gekauft markieren',
        'premium_title': '⭐ FamFood Premium',
        'premium_desc': 'Schalten Sie +500 Rezepte, KI-Vorschläge und mehr frei',
        'premium_price': '3,99€/Monat',
        'try_free': '7 Tage kostenlos testen',
        'nuts': 'Nüsse',
        'gluten': 'Gluten',
        'lactose': 'Laktose',
        'eggs': 'Eier',
        'shellfish': 'Meeresfrüchte',
        'none': 'Keine',
        'min': 'min',
        'welcome': 'Willkommen bei FamFood!',
        'welcome_text': 'Planen Sie einfach die Mahlzeiten Ihrer Familie und sparen Sie Zeit und Geld.',
    }
}

# =====================================================
# RECETAS POR IDIOMA/PAÍS
# =====================================================

RECIPES = {
    'es': [
        {'id': 1, 'name': 'Tortilla Española', 'category': 'vegetables', 'time': 30, 'difficulty': 'easy', 'servings': 4, 'image': '🥚', 
         'ingredients': ['6 huevos', '4 patatas medianas', '1 cebolla', 'Aceite de oliva', 'Sal'],
         'instructions': '1. Cortar patatas y cebolla. 2. Freír a fuego lento. 3. Batir huevos y mezclar. 4. Cuajar en sartén.',
         'cost': 4.50},
        {'id': 2, 'name': 'Paella Valenciana', 'category': 'meat', 'time': 60, 'difficulty': 'medium', 'servings': 6, 'image': '🥘',
         'ingredients': ['400g arroz', '500g pollo', '200g judías verdes', 'Azafrán', 'Caldo de pollo', 'Aceite', 'Sal'],
         'instructions': '1. Sofreír pollo. 2. Añadir verduras. 3. Agregar arroz y caldo. 4. Cocer 20 min sin remover.',
         'cost': 12.00},
        {'id': 3, 'name': 'Gazpacho Andaluz', 'category': 'soups', 'time': 15, 'difficulty': 'easy', 'servings': 4, 'image': '🍅',
         'ingredients': ['1kg tomates maduros', '1 pepino', '1 pimiento', '1 diente de ajo', 'Vinagre', 'Aceite', 'Sal'],
         'instructions': '1. Trocear verduras. 2. Triturar todo. 3. Añadir aceite, vinagre y sal. 4. Enfriar 2 horas.',
         'cost': 3.50},
        {'id': 4, 'name': 'Lentejas con Chorizo', 'category': 'soups', 'time': 45, 'difficulty': 'easy', 'servings': 6, 'image': '🍲',
         'ingredients': ['400g lentejas', '1 chorizo', '2 zanahorias', '1 cebolla', '2 patatas', 'Laurel', 'Sal'],
         'instructions': '1. Poner lentejas en agua. 2. Añadir verduras y chorizo. 3. Cocer 45 min. 4. Sal al final.',
         'cost': 5.00},
        {'id': 5, 'name': 'Pollo al Ajillo', 'category': 'meat', 'time': 35, 'difficulty': 'easy', 'servings': 4, 'image': '🍗',
         'ingredients': ['1 pollo troceado', '10 dientes de ajo', 'Vino blanco', 'Aceite de oliva', 'Perejil', 'Sal'],
         'instructions': '1. Dorar pollo. 2. Añadir ajos laminados. 3. Verter vino. 4. Cocer tapado 25 min.',
         'cost': 7.00},
        {'id': 6, 'name': 'Merluza en Salsa Verde', 'category': 'fish', 'time': 25, 'difficulty': 'easy', 'servings': 4, 'image': '🐟',
         'ingredients': ['4 rodajas merluza', '4 dientes de ajo', 'Perejil fresco', 'Vino blanco', 'Aceite', 'Sal'],
         'instructions': '1. Dorar ajos en aceite. 2. Añadir merluza. 3. Verter vino y perejil. 4. Cocer 10 min moviendo cazuela.',
         'cost': 10.00},
        {'id': 7, 'name': 'Espaguetis Carbonara', 'category': 'pasta', 'time': 20, 'difficulty': 'easy', 'servings': 4, 'image': '🍝',
         'ingredients': ['400g espaguetis', '200g bacon', '3 huevos', '100g parmesano', 'Pimienta negra', 'Sal'],
         'instructions': '1. Cocer pasta. 2. Freír bacon. 3. Mezclar huevos y queso. 4. Unir todo fuera del fuego.',
         'cost': 6.00},
        {'id': 8, 'name': 'Croquetas de Jamón', 'category': 'meat', 'time': 60, 'difficulty': 'medium', 'servings': 6, 'image': '🍖',
         'ingredients': ['100g jamón serrano', '50g mantequilla', '50g harina', '500ml leche', 'Huevo', 'Pan rallado'],
         'instructions': '1. Hacer bechamel. 2. Añadir jamón. 3. Enfriar 4 horas. 4. Formar, rebozar y freír.',
         'cost': 8.00},
        {'id': 9, 'name': 'Ensalada César', 'category': 'vegetables', 'time': 15, 'difficulty': 'easy', 'servings': 4, 'image': '🥗',
         'ingredients': ['1 lechuga romana', '100g parmesano', 'Picatostes', 'Pechuga de pollo', 'Salsa César'],
         'instructions': '1. Cortar lechuga. 2. Grillar pollo y cortar. 3. Mezclar todo. 4. Aliñar con salsa.',
         'cost': 5.50},
        {'id': 10, 'name': 'Albóndigas en Salsa', 'category': 'meat', 'time': 40, 'difficulty': 'easy', 'servings': 4, 'image': '🍖',
         'ingredients': ['500g carne picada', '1 huevo', 'Pan rallado', 'Tomate frito', 'Cebolla', 'Ajo', 'Sal'],
         'instructions': '1. Mezclar carne, huevo y pan. 2. Formar bolas. 3. Freír. 4. Cocer en salsa de tomate 20 min.',
         'cost': 6.50},
        {'id': 11, 'name': 'Macarrones con Tomate', 'category': 'pasta', 'time': 20, 'difficulty': 'easy', 'servings': 4, 'image': '🍝',
         'ingredients': ['400g macarrones', '400g tomate frito', '100g queso rallado', 'Orégano', 'Sal'],
         'instructions': '1. Cocer pasta al dente. 2. Calentar tomate. 3. Mezclar. 4. Servir con queso.',
         'cost': 3.50},
        {'id': 12, 'name': 'Pisto Manchego', 'category': 'vegetables', 'time': 40, 'difficulty': 'easy', 'servings': 4, 'image': '🥬',
         'ingredients': ['2 calabacines', '2 pimientos', '1 cebolla', '3 tomates', 'Aceite', 'Sal'],
         'instructions': '1. Cortar verduras en dados. 2. Sofreír cebolla. 3. Añadir resto. 4. Cocer a fuego lento 30 min.',
         'cost': 4.00},
    ],
    'en': [
        {'id': 101, 'name': 'Shepherd\'s Pie', 'category': 'meat', 'time': 60, 'difficulty': 'medium', 'servings': 6, 'image': '🥧',
         'ingredients': ['500g minced lamb', '4 potatoes', '1 onion', '2 carrots', 'Peas', 'Gravy', 'Butter'],
         'instructions': '1. Cook mince with vegetables. 2. Make mashed potatoes. 3. Layer in dish. 4. Bake 25 min.',
         'cost': 9.00},
        {'id': 102, 'name': 'Fish and Chips', 'category': 'fish', 'time': 40, 'difficulty': 'medium', 'servings': 4, 'image': '🐟',
         'ingredients': ['4 cod fillets', '200g flour', 'Beer', 'Potatoes', 'Oil for frying', 'Salt'],
         'instructions': '1. Make batter with flour and beer. 2. Cut chips and fry. 3. Coat fish and fry. 4. Serve with peas.',
         'cost': 11.00},
        {'id': 103, 'name': 'Chicken Tikka Masala', 'category': 'meat', 'time': 45, 'difficulty': 'medium', 'servings': 4, 'image': '🍗',
         'ingredients': ['500g chicken', 'Tikka paste', 'Coconut milk', 'Onion', 'Tomatoes', 'Rice', 'Coriander'],
         'instructions': '1. Marinate chicken. 2. Grill chicken. 3. Make sauce with paste and coconut. 4. Combine and serve with rice.',
         'cost': 8.50},
        {'id': 104, 'name': 'Spaghetti Bolognese', 'category': 'pasta', 'time': 45, 'difficulty': 'easy', 'servings': 4, 'image': '🍝',
         'ingredients': ['400g spaghetti', '500g beef mince', 'Tomato sauce', 'Onion', 'Garlic', 'Italian herbs', 'Parmesan'],
         'instructions': '1. Fry mince with onion. 2. Add tomatoes and herbs. 3. Simmer 30 min. 4. Serve over pasta.',
         'cost': 7.00},
        {'id': 105, 'name': 'Roast Chicken', 'category': 'meat', 'time': 90, 'difficulty': 'easy', 'servings': 6, 'image': '🍗',
         'ingredients': ['1 whole chicken', 'Potatoes', 'Carrots', 'Onion', 'Butter', 'Thyme', 'Salt'],
         'instructions': '1. Season chicken. 2. Surround with vegetables. 3. Roast 1h 20min at 180°C. 4. Rest before carving.',
         'cost': 10.00},
        {'id': 106, 'name': 'Bangers and Mash', 'category': 'meat', 'time': 30, 'difficulty': 'easy', 'servings': 4, 'image': '🌭',
         'ingredients': ['8 sausages', '4 potatoes', 'Butter', 'Milk', 'Onion gravy', 'Peas'],
         'instructions': '1. Cook sausages. 2. Boil and mash potatoes. 3. Make gravy. 4. Serve together.',
         'cost': 6.00},
        {'id': 107, 'name': 'Caesar Salad', 'category': 'vegetables', 'time': 15, 'difficulty': 'easy', 'servings': 4, 'image': '🥗',
         'ingredients': ['Romaine lettuce', 'Parmesan', 'Croutons', 'Chicken breast', 'Caesar dressing'],
         'instructions': '1. Chop lettuce. 2. Grill and slice chicken. 3. Toss everything. 4. Add dressing.',
         'cost': 5.50},
        {'id': 108, 'name': 'Beef Stew', 'category': 'meat', 'time': 120, 'difficulty': 'medium', 'servings': 6, 'image': '🍲',
         'ingredients': ['600g beef chunks', 'Potatoes', 'Carrots', 'Onion', 'Beef stock', 'Tomato paste', 'Herbs'],
         'instructions': '1. Brown beef. 2. Add vegetables. 3. Pour stock. 4. Slow cook 2 hours.',
         'cost': 11.00},
        {'id': 109, 'name': 'Macaroni Cheese', 'category': 'pasta', 'time': 30, 'difficulty': 'easy', 'servings': 4, 'image': '🧀',
         'ingredients': ['400g macaroni', 'Cheddar cheese', 'Butter', 'Flour', 'Milk', 'Mustard'],
         'instructions': '1. Cook pasta. 2. Make cheese sauce. 3. Mix together. 4. Bake until golden.',
         'cost': 4.50},
        {'id': 110, 'name': 'Toad in the Hole', 'category': 'meat', 'time': 45, 'difficulty': 'easy', 'servings': 4, 'image': '🌭',
         'ingredients': ['8 sausages', 'Flour', 'Eggs', 'Milk', 'Oil', 'Gravy'],
         'instructions': '1. Make Yorkshire batter. 2. Heat oil in tin. 3. Add sausages and batter. 4. Bake 35 min.',
         'cost': 5.50},
    ],
    'fr': [
        {'id': 201, 'name': 'Quiche Lorraine', 'category': 'meat', 'time': 50, 'difficulty': 'medium', 'servings': 6, 'image': '🥧',
         'ingredients': ['Pâte brisée', '200g lardons', '3 œufs', '200ml crème fraîche', 'Gruyère', 'Muscade'],
         'instructions': '1. Foncer le moule. 2. Faire revenir lardons. 3. Mélanger œufs et crème. 4. Cuire 35 min à 180°C.',
         'cost': 7.00},
        {'id': 202, 'name': 'Ratatouille', 'category': 'vegetables', 'time': 45, 'difficulty': 'easy', 'servings': 6, 'image': '🥬',
         'ingredients': ['2 courgettes', '2 aubergines', '3 tomates', '2 poivrons', 'Oignon', 'Ail', 'Herbes de Provence'],
         'instructions': '1. Couper légumes. 2. Faire revenir oignon. 3. Ajouter légumes. 4. Mijoter 40 min.',
         'cost': 5.00},
        {'id': 203, 'name': 'Boeuf Bourguignon', 'category': 'meat', 'time': 180, 'difficulty': 'hard', 'servings': 6, 'image': '🍲',
         'ingredients': ['1kg boeuf', 'Vin rouge', 'Lardons', 'Champignons', 'Carottes', 'Oignons', 'Bouquet garni'],
         'instructions': '1. Mariner viande. 2. Faire revenir. 3. Ajouter vin et légumes. 4. Mijoter 3 heures.',
         'cost': 15.00},
        {'id': 204, 'name': 'Croque-Monsieur', 'category': 'quick', 'time': 15, 'difficulty': 'easy', 'servings': 2, 'image': '🥪',
         'ingredients': ['4 tranches pain de mie', 'Jambon', 'Gruyère', 'Béchamel', 'Beurre'],
         'instructions': '1. Beurrer pain. 2. Garnir jambon et fromage. 3. Napper béchamel. 4. Gratiner 10 min.',
         'cost': 4.00},
        {'id': 205, 'name': 'Poulet Rôti', 'category': 'meat', 'time': 75, 'difficulty': 'easy', 'servings': 6, 'image': '🍗',
         'ingredients': ['1 poulet', 'Pommes de terre', 'Beurre', 'Thym', 'Ail', 'Sel'],
         'instructions': '1. Assaisonner poulet. 2. Entourer de pommes de terre. 3. Rôtir 1h15 à 180°C. 4. Arroser régulièrement.',
         'cost': 10.00},
        {'id': 206, 'name': 'Soupe à l\'Oignon', 'category': 'soups', 'time': 45, 'difficulty': 'easy', 'servings': 4, 'image': '🍲',
         'ingredients': ['6 oignons', 'Beurre', 'Bouillon de boeuf', 'Pain', 'Gruyère', 'Vin blanc'],
         'instructions': '1. Caraméliser oignons. 2. Ajouter bouillon et vin. 3. Servir avec pain et fromage gratiné.',
         'cost': 4.50},
        {'id': 207, 'name': 'Gratin Dauphinois', 'category': 'vegetables', 'time': 60, 'difficulty': 'easy', 'servings': 6, 'image': '🥔',
         'ingredients': ['1kg pommes de terre', '500ml crème', 'Ail', 'Beurre', 'Muscade', 'Sel'],
         'instructions': '1. Couper pommes de terre fines. 2. Frotter plat avec ail. 3. Superposer et napper crème. 4. Cuire 1h.',
         'cost': 5.00},
        {'id': 208, 'name': 'Blanquette de Veau', 'category': 'meat', 'time': 90, 'difficulty': 'medium', 'servings': 6, 'image': '🍖',
         'ingredients': ['1kg veau', 'Carottes', 'Poireaux', 'Champignons', 'Crème', 'Jaune d\'œuf', 'Bouquet garni'],
         'instructions': '1. Pocher viande. 2. Cuire légumes. 3. Faire sauce crème. 4. Assembler le tout.',
         'cost': 14.00},
    ],
    'de': [
        {'id': 301, 'name': 'Wiener Schnitzel', 'category': 'meat', 'time': 30, 'difficulty': 'easy', 'servings': 4, 'image': '🍖',
         'ingredients': ['4 Kalbsschnitzel', 'Mehl', 'Eier', 'Semmelbrösel', 'Butter', 'Zitrone', 'Salz'],
         'instructions': '1. Schnitzel klopfen. 2. Panieren: Mehl, Ei, Brösel. 3. In Butter goldbraun braten. 4. Mit Zitrone servieren.',
         'cost': 12.00},
        {'id': 302, 'name': 'Kartoffelsalat', 'category': 'vegetables', 'time': 30, 'difficulty': 'easy', 'servings': 6, 'image': '🥔',
         'ingredients': ['1kg Kartoffeln', 'Zwiebel', 'Brühe', 'Essig', 'Öl', 'Senf', 'Schnittlauch'],
         'instructions': '1. Kartoffeln kochen und schneiden. 2. Warme Brühe darüber. 3. Mit Essig und Öl anmachen. 4. Ziehen lassen.',
         'cost': 3.50},
        {'id': 303, 'name': 'Sauerbraten', 'category': 'meat', 'time': 180, 'difficulty': 'hard', 'servings': 6, 'image': '🍖',
         'ingredients': ['1kg Rinderbraten', 'Rotwein', 'Essig', 'Zwiebeln', 'Möhren', 'Lebkuchen', 'Gewürze'],
         'instructions': '1. Fleisch 3 Tage marinieren. 2. Anbraten. 3. Mit Marinade schmoren. 4. Soße mit Lebkuchen binden.',
         'cost': 16.00},
        {'id': 304, 'name': 'Bratwurst mit Sauerkraut', 'category': 'meat', 'time': 25, 'difficulty': 'easy', 'servings': 4, 'image': '🌭',
         'ingredients': ['8 Bratwürste', '500g Sauerkraut', 'Zwiebel', 'Apfel', 'Kümmel', 'Brühe'],
         'instructions': '1. Würste braten. 2. Sauerkraut mit Apfel und Zwiebel dünsten. 3. Zusammen servieren.',
         'cost': 7.00},
        {'id': 305, 'name': 'Käsespätzle', 'category': 'pasta', 'time': 40, 'difficulty': 'medium', 'servings': 4, 'image': '🧀',
         'ingredients': ['400g Spätzle', '200g Bergkäse', 'Zwiebeln', 'Butter', 'Schnittlauch', 'Salz'],
         'instructions': '1. Spätzle kochen. 2. Mit Käse schichten. 3. Röstzwiebeln darüber. 4. Im Ofen überbacken.',
         'cost': 6.00},
        {'id': 306, 'name': 'Gulaschsuppe', 'category': 'soups', 'time': 90, 'difficulty': 'medium', 'servings': 6, 'image': '🍲',
         'ingredients': ['500g Rindfleisch', 'Paprika', 'Zwiebeln', 'Tomaten', 'Kartoffeln', 'Paprikapulver', 'Kümmel'],
         'instructions': '1. Fleisch anbraten. 2. Zwiebeln und Paprika dazu. 3. Mit Brühe aufgießen. 4. 1 Stunde köcheln.',
         'cost': 8.00},
        {'id': 307, 'name': 'Königsberger Klopse', 'category': 'meat', 'time': 45, 'difficulty': 'medium', 'servings': 4, 'image': '🍖',
         'ingredients': ['500g Hackfleisch', 'Brötchen', 'Ei', 'Sardellen', 'Kapern', 'Zitrone', 'Sahne'],
         'instructions': '1. Fleischklöße formen. 2. In Brühe garen. 3. Weiße Soße mit Kapern machen. 4. Klöße darin servieren.',
         'cost': 9.00},
        {'id': 308, 'name': 'Reibekuchen', 'category': 'vegetables', 'time': 30, 'difficulty': 'easy', 'servings': 4, 'image': '🥔',
         'ingredients': ['1kg Kartoffeln', '1 Zwiebel', '2 Eier', 'Mehl', 'Salz', 'Öl', 'Apfelmus'],
         'instructions': '1. Kartoffeln reiben. 2. Mit Ei und Mehl mischen. 3. Flache Kuchen braten. 4. Mit Apfelmus servieren.',
         'cost': 4.00},
    ]
}

# =====================================================
# INICIALIZAR ESTADO
# =====================================================

if 'language' not in st.session_state:
    st.session_state.language = 'es'

if 'weekly_menu' not in st.session_state:
    st.session_state.weekly_menu = {
        'monday': {'lunch': None, 'dinner': None},
        'tuesday': {'lunch': None, 'dinner': None},
        'wednesday': {'lunch': None, 'dinner': None},
        'thursday': {'lunch': None, 'dinner': None},
        'friday': {'lunch': None, 'dinner': None},
        'saturday': {'lunch': None, 'dinner': None},
        'sunday': {'lunch': None, 'dinner': None},
    }

if 'family' not in st.session_state:
    st.session_state.family = {
        'people': 4,
        'budget': 100,
        'allergies': [],
        'preferences': []
    }

if 'shopping_list' not in st.session_state:
    st.session_state.shopping_list = []

# =====================================================
# FUNCIONES AUXILIARES
# =====================================================

def t(key):
    """Obtiene traducción"""
    return TRANSLATIONS[st.session_state.language].get(key, key)

def get_recipes():
    """Obtiene recetas del idioma actual + internacionales"""
    lang = st.session_state.language
    recipes = RECIPES.get(lang, RECIPES['en']).copy()
    return recipes

def generate_automatic_menu():
    """Genera un menú automático aleatorio"""
    recipes = get_recipes()
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    for day in days:
        lunch_recipe = random.choice(recipes)
        dinner_recipe = random.choice([r for r in recipes if r['id'] != lunch_recipe['id']])
        st.session_state.weekly_menu[day]['lunch'] = lunch_recipe
        st.session_state.weekly_menu[day]['dinner'] = dinner_recipe

def clear_menu():
    """Limpia el menú"""
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    for day in days:
        st.session_state.weekly_menu[day]['lunch'] = None
        st.session_state.weekly_menu[day]['dinner'] = None

def generate_shopping_list():
    """Genera lista de compra del menú"""
    ingredients = {}
    
    for day, meals in st.session_state.weekly_menu.items():
        for meal_type, recipe in meals.items():
            if recipe:
                for ing in recipe.get('ingredients', []):
                    if ing in ingredients:
                        ingredients[ing] += 1
                    else:
                        ingredients[ing] = 1
    
    st.session_state.shopping_list = [{'item': k, 'quantity': v, 'bought': False} for k, v in ingredients.items()]

def get_total_cost():
    """Calcula coste total del menú"""
    total = 0
    for day, meals in st.session_state.weekly_menu.items():
        for meal_type, recipe in meals.items():
            if recipe:
                total += recipe.get('cost', 0)
    return total

# =====================================================
# CSS PERSONALIZADO
# =====================================================

st.markdown("""
<style>
    /* Colores principales - Naranja */
    :root {
        --primary-color: #FF6B35;
        --primary-light: #FFF0EB;
        --primary-dark: #E55A2B;
    }
    
    /* Header */
    .main-header {
        background: linear-gradient(135deg, #FF6B35 0%, #F7931E 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin-bottom: 1rem;
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
    }
    
    /* Cards de recetas */
    .recipe-card {
        background: white;
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border-left: 4px solid #FF6B35;
    }
    
    .recipe-card:hover {
        box-shadow: 0 4px 12px rgba(255,107,53,0.2);
    }
    
    /* Menu semanal */
    .day-card {
        background: linear-gradient(180deg, #FFF8F5 0%, #FFFFFF 100%);
        border-radius: 10px;
        padding: 0.8rem;
        text-align: center;
        border: 1px solid #FFE0D5;
    }
    
    .day-card h4 {
        color: #FF6B35;
        margin-bottom: 0.5rem;
    }
    
    .meal-slot {
        background: white;
        border-radius: 8px;
        padding: 0.5rem;
        margin: 0.3rem 0;
        min-height: 60px;
        border: 2px dashed #FFD5C5;
    }
    
    .meal-slot.filled {
        border: 2px solid #FF6B35;
        background: #FFF8F5;
    }
    
    /* Lista de compra */
    .shopping-item {
        display: flex;
        align-items: center;
        padding: 0.5rem;
        border-bottom: 1px solid #eee;
    }
    
    .shopping-item.bought {
        text-decoration: line-through;
        opacity: 0.5;
    }
    
    /* Botones */
    .stButton > button {
        background: linear-gradient(135deg, #FF6B35 0%, #F7931E 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #E55A2B 0%, #E8820A 100%);
    }
    
    /* Premium banner */
    .premium-banner {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 12px;
        padding: 1rem;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #FFF8F5 0%, #FFFFFF 100%);
    }
    
    /* Emoji grande para recetas */
    .recipe-emoji {
        font-size: 3rem;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    /* Ocultar menu hamburguesa */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:
    # Logo y nombre
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0;">
        <span style="font-size: 3rem;">🍽️</span>
        <h1 style="color: #FF6B35; margin: 0;">FamFood</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # Selector de idioma
    st.markdown(f"### 🌍 {t('language')}")
    lang_options = {'es': '🇪🇸 Español', 'en': '🇬🇧 English', 'fr': '🇫🇷 Français', 'de': '🇩🇪 Deutsch'}
    selected_lang = st.selectbox(
        "Idioma",
        options=list(lang_options.keys()),
        format_func=lambda x: lang_options[x],
        index=list(lang_options.keys()).index(st.session_state.language),
        label_visibility="collapsed"
    )
    
    if selected_lang != st.session_state.language:
        st.session_state.language = selected_lang
        st.rerun()
    
    st.divider()
    
    # Navegación
    page = st.radio(
        "Navegación",
        [t('weekly_menu'), t('recipes'), t('shopping_list'), t('family')],
        label_visibility="collapsed"
    )
    
    st.divider()
    
    # Info familia rápida
    st.markdown(f"### 👨‍👩‍👧‍👦 {t('family')}")
    st.write(f"**{t('people')}:** {st.session_state.family['people']}")
    st.write(f"**{t('budget')}:** {st.session_state.family['budget']}€")
    
    # Coste actual del menú
    current_cost = get_total_cost()
    if current_cost > 0:
        st.metric(t('estimated_cost'), f"{current_cost:.2f}€")

# =====================================================
# CONTENIDO PRINCIPAL
# =====================================================

# Header principal
st.markdown(f"""
<div class="main-header">
    <h1>🍽️ FamFood</h1>
    <p>{t('tagline')}</p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# PÁGINA: MENÚ SEMANAL
# =====================================================

if page == t('weekly_menu'):
    
    # Botones de acción
    col1, col2, col3 = st.columns([1, 1, 2])
    with col1:
        if st.button(t('generate_menu'), use_container_width=True):
            generate_automatic_menu()
            st.rerun()
    with col2:
        if st.button(t('clear_menu'), use_container_width=True):
            clear_menu()
            st.rerun()
    
    st.divider()
    
    # Calendario semanal
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day_names = [t('monday'), t('tuesday'), t('wednesday'), t('thursday'), t('friday'), t('saturday'), t('sunday')]
    
    # Crear columnas para cada día
    cols = st.columns(7)
    
    for i, (day, day_name) in enumerate(zip(days, day_names)):
        with cols[i]:
            st.markdown(f"### {day_name[:3]}")
            
            # Comida
            st.caption(f"🌞 {t('lunch')}")
            lunch = st.session_state.weekly_menu[day]['lunch']
            if lunch:
                st.markdown(f"""
                <div style="background:#FFF8F5; padding:8px; border-radius:8px; text-align:center; border:2px solid #FF6B35;">
                    <span style="font-size:1.5rem;">{lunch['image']}</span><br>
                    <small>{lunch['name'][:15]}...</small>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style="background:#f5f5f5; padding:8px; border-radius:8px; text-align:center; min-height:60px; border:2px dashed #ddd;">
                    <span style="color:#aaa;">+</span>
                </div>
                """, unsafe_allow_html=True)
            
            # Cena
            st.caption(f"🌙 {t('dinner')}")
            dinner = st.session_state.weekly_menu[day]['dinner']
            if dinner:
                st.markdown(f"""
                <div style="background:#FFF8F5; padding:8px; border-radius:8px; text-align:center; border:2px solid #FF6B35;">
                    <span style="font-size:1.5rem;">{dinner['image']}</span><br>
                    <small>{dinner['name'][:15]}...</small>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div style="background:#f5f5f5; padding:8px; border-radius:8px; text-align:center; min-height:60px; border:2px dashed #ddd;">
                    <span style="color:#aaa;">+</span>
                </div>
                """, unsafe_allow_html=True)
    
    st.divider()
    
    # Resumen del menú
    col1, col2, col3 = st.columns(3)
    
    meals_count = sum(1 for day in st.session_state.weekly_menu.values() 
                      for meal in day.values() if meal is not None)
    
    with col1:
        st.metric("🍽️ Comidas planificadas", f"{meals_count}/14")
    with col2:
        st.metric(f"💰 {t('estimated_cost')}", f"{get_total_cost():.2f}€")
    with col3:
        if st.button(f"🛒 {t('generate_list')}", use_container_width=True):
            generate_shopping_list()
            st.success("✅ Lista generada!")

# =====================================================
# PÁGINA: RECETAS
# =====================================================

elif page == t('recipes'):
    
    # Buscador y filtros
    col1, col2 = st.columns([2, 1])
    with col1:
        search = st.text_input("🔍", placeholder=t('search_recipe'), label_visibility="collapsed")
    with col2:
        category = st.selectbox(
            "Categoría",
            ['all', 'meat', 'fish', 'vegetables', 'pasta', 'soups', 'quick'],
            format_func=lambda x: t('all_categories') if x == 'all' else t(x),
            label_visibility="collapsed"
        )
    
    st.divider()
    
    # Obtener y filtrar recetas
    recipes = get_recipes()
    
    if search:
        recipes = [r for r in recipes if search.lower() in r['name'].lower()]
    
    if category != 'all':
        recipes = [r for r in recipes if r['category'] == category]
    
    # Mostrar recetas en grid
    cols = st.columns(3)
    
    for i, recipe in enumerate(recipes):
        with cols[i % 3]:
            with st.container():
                st.markdown(f"""
                <div class="recipe-card">
                    <div class="recipe-emoji">{recipe['image']}</div>
                    <h4 style="margin:0; color:#333;">{recipe['name']}</h4>
                    <p style="color:#888; font-size:0.8rem; margin:0.5rem 0;">
                        ⏱️ {recipe['time']} {t('min')} · 👥 {recipe['servings']} · 💰 {recipe['cost']}€
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                with st.expander("Ver receta"):
                    st.write(f"**{t('ingredients')}:**")
                    for ing in recipe['ingredients']:
                        st.write(f"• {ing}")
                    st.write(f"**{t('instructions')}:**")
                    st.write(recipe['instructions'])
                    
                    # Selector de día y comida para añadir
                    col_a, col_b = st.columns(2)
                    with col_a:
                        day_to_add = st.selectbox(
                            "Día",
                            ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'],
                            format_func=lambda x: t(x),
                            key=f"day_{recipe['id']}"
                        )
                    with col_b:
                        meal_to_add = st.selectbox(
                            "Comida",
                            ['lunch', 'dinner'],
                            format_func=lambda x: t(x),
                            key=f"meal_{recipe['id']}"
                        )
                    
                    if st.button(t('add_to_menu'), key=f"add_{recipe['id']}"):
                        st.session_state.weekly_menu[day_to_add][meal_to_add] = recipe
                        st.success(f"✅ {recipe['name']} añadido!")

# =====================================================
# PÁGINA: LISTA DE COMPRA
# =====================================================

elif page == t('shopping_list'):
    
    if not st.session_state.shopping_list:
        st.info(f"📝 Genera primero tu menú semanal y luego pulsa '{t('generate_list')}'")
        
        if st.button(t('generate_list')):
            generate_shopping_list()
            st.rerun()
    else:
        # Botones de acción
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Regenerar lista"):
                generate_shopping_list()
                st.rerun()
        with col2:
            # Crear texto para WhatsApp
            shopping_text = "🛒 *Lista de la compra - FamFood*\n\n"
            for item in st.session_state.shopping_list:
                check = "✅" if item['bought'] else "⬜"
                shopping_text += f"{check} {item['item']}\n"
            
            whatsapp_url = f"https://wa.me/?text={shopping_text}"
            st.markdown(f"[{t('share_whatsapp')}]({whatsapp_url})")
        
        st.divider()
        
        # Categorizar items (simplificado)
        categories = {
            t('meat'): ['pollo', 'carne', 'jamón', 'bacon', 'chorizo', 'chicken', 'beef', 'pork', 'lamb', 'sausage', 'poulet', 'viande', 'Fleisch', 'Hähnchen', 'lardons'],
            t('fish'): ['merluza', 'pescado', 'fish', 'cod', 'salmon', 'poisson', 'Fisch'],
            t('vegetables'): ['tomate', 'cebolla', 'patata', 'lechuga', 'zanahoria', 'pimiento', 'potato', 'onion', 'carrot', 'lettuce', 'pomme de terre', 'oignon', 'Kartoffel', 'Zwiebel'],
            t('dairy'): ['leche', 'queso', 'huevo', 'mantequilla', 'nata', 'milk', 'cheese', 'egg', 'butter', 'cream', 'lait', 'fromage', 'œuf', 'beurre', 'Milch', 'Käse', 'Ei', 'Butter'],
            t('others'): []
        }
        
        # Mostrar items
        for item in st.session_state.shopping_list:
            col1, col2 = st.columns([4, 1])
            with col1:
                bought = st.checkbox(
                    item['item'],
                    value=item['bought'],
                    key=f"item_{item['item']}"
                )
                item['bought'] = bought
            with col2:
                st.write(f"x{item['quantity']}")
        
        # Resumen
        st.divider()
        total_items = len(st.session_state.shopping_list)
        bought_items = sum(1 for item in st.session_state.shopping_list if item['bought'])
        st.progress(bought_items / total_items if total_items > 0 else 0)
        st.write(f"✅ {bought_items}/{total_items} items comprados")

# =====================================================
# PÁGINA: FAMILIA
# =====================================================

elif page == t('family'):
    
    st.subheader(f"👨‍👩‍👧‍👦 {t('family')}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Número de personas
        people = st.number_input(
            t('people'),
            min_value=1,
            max_value=12,
            value=st.session_state.family['people']
        )
        st.session_state.family['people'] = people
        
        # Presupuesto
        budget = st.number_input(
            f"{t('budget')} (€)",
            min_value=20,
            max_value=500,
            value=st.session_state.family['budget'],
            step=10
        )
        st.session_state.family['budget'] = budget
    
    with col2:
        # Alergias
        st.write(f"**⚠️ {t('allergies')}**")
        allergies = []
        for allergy in ['gluten', 'lactose', 'nuts', 'eggs', 'shellfish']:
            if st.checkbox(t(allergy), key=f"allergy_{allergy}"):
                allergies.append(allergy)
        st.session_state.family['allergies'] = allergies
    
    st.divider()
    
    # Preferencias
    st.write(f"**🍽️ {t('preferences')}**")
    col1, col2 = st.columns(2)
    
    preferences = []
    with col1:
        if st.checkbox(t('no_pork')):
            preferences.append('no_pork')
        if st.checkbox(t('vegetarian')):
            preferences.append('vegetarian')
    with col2:
        if st.checkbox(t('no_spicy')):
            preferences.append('no_spicy')
        if st.checkbox(t('quick_meals')):
            preferences.append('quick_meals')
    
    st.session_state.family['preferences'] = preferences
    
    st.divider()
    
    # Banner Premium
    st.markdown(f"""
    <div class="premium-banner">
        <h3>{t('premium_title')}</h3>
        <p>{t('premium_desc')}</p>
        <p style="font-size: 1.5rem; font-weight: bold;">{t('premium_price')}</p>
        <button style="background: white; color: #667eea; border: none; padding: 0.5rem 2rem; border-radius: 20px; font-weight: bold; cursor: pointer;">
            {t('try_free')}
        </button>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.divider()
st.markdown("""
<div style="text-align: center; color: #888; padding: 1rem;">
    <p>🍽️ <strong>FamFood</strong> v1.0</p>
    <p style="font-size: 0.8rem;">Planifica • Cocina • Disfruta en familia</p>
</div>
""", unsafe_allow_html=True)
