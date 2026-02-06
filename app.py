"""
🍽️ FamFood PRO - Planificador de Menú Familiar Inteligente
Inspirado en INDYA - Versión completa multi-idioma
500+ recetas | Info nutricional | IA integrada | 4 idiomas
"""

import streamlit as st
import random
from datetime import datetime, timedelta
import json

# =====================================================
# CONFIGURACIÓN
# =====================================================

st.set_page_config(
    page_title="FamFood - Smart Meal Planner",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# TRADUCCIONES COMPLETAS
# =====================================================

TRANSLATIONS = {
    'es': {
        # General
        'app_name': 'FamFood',
        'tagline': 'Tu planificador de menú familiar inteligente',
        'welcome': '¡Bienvenido a FamFood!',
        'welcome_text': 'Planifica las comidas de tu familia, ahorra tiempo y come mejor.',
        
        # Navegación
        'nav_menu': '📅 Menú Semanal',
        'nav_recipes': '🍳 Recetas',
        'nav_shopping': '🛒 Lista Compra',
        'nav_family': '👨‍👩‍👧‍👦 Mi Familia',
        'nav_ai': '🤖 Asistente IA',
        'nav_favorites': '⭐ Favoritos',
        
        # Menú semanal
        'week_of': 'Semana del',
        'generate_menu': '🎲 Generar menú automático',
        'clear_menu': '🗑️ Limpiar todo',
        'copy_week': '📋 Copiar semana anterior',
        'lunch': 'Comida',
        'dinner': 'Cena',
        'breakfast': 'Desayuno',
        'snack': 'Merienda',
        'empty_slot': 'Toca para añadir',
        'change_recipe': '🔄 Cambiar',
        'remove_recipe': '❌ Quitar',
        
        # Días
        'monday': 'Lunes', 'tuesday': 'Martes', 'wednesday': 'Miércoles',
        'thursday': 'Jueves', 'friday': 'Viernes', 'saturday': 'Sábado', 'sunday': 'Domingo',
        'mon': 'Lun', 'tue': 'Mar', 'wed': 'Mié', 'thu': 'Jue', 'fri': 'Vie', 'sat': 'Sáb', 'sun': 'Dom',
        
        # Recetas
        'search_recipes': 'Buscar recetas...',
        'all_categories': 'Todas',
        'filter_time': 'Tiempo máximo',
        'filter_difficulty': 'Dificultad',
        'filter_calories': 'Calorías máx.',
        'sort_by': 'Ordenar por',
        'sort_name': 'Nombre',
        'sort_time': 'Tiempo',
        'sort_calories': 'Calorías',
        'sort_rating': 'Valoración',
        'prep_time': 'Preparación',
        'cook_time': 'Cocción',
        'total_time': 'Tiempo total',
        'servings': 'Raciones',
        'difficulty': 'Dificultad',
        'calories': 'Calorías',
        'proteins': 'Proteínas',
        'carbs': 'Carbohidratos',
        'fats': 'Grasas',
        'fiber': 'Fibra',
        'ingredients': 'Ingredientes',
        'instructions': 'Preparación',
        'tips': 'Consejos',
        'nutrition_info': 'Información nutricional',
        'per_serving': 'Por ración',
        'add_to_menu': '➕ Añadir al menú',
        'add_to_favorites': '⭐ Añadir a favoritos',
        'remove_from_favorites': '💔 Quitar de favoritos',
        'similar_recipes': 'Recetas similares',
        'view_recipe': 'Ver receta',
        
        # Categorías
        'cat_all': '🍽️ Todas',
        'cat_meat': '🥩 Carnes',
        'cat_fish': '🐟 Pescados',
        'cat_vegetarian': '🥬 Vegetariano',
        'cat_pasta': '🍝 Pastas',
        'cat_rice': '🍚 Arroces',
        'cat_soup': '🍲 Sopas y cremas',
        'cat_salad': '🥗 Ensaladas',
        'cat_eggs': '🥚 Huevos',
        'cat_legumes': '🫘 Legumbres',
        'cat_quick': '⚡ Rápidas (<20 min)',
        'cat_kids': '👶 Para niños',
        'cat_healthy': '💚 Saludables',
        'cat_comfort': '🏠 Comfort food',
        'cat_international': '🌍 Internacional',
        
        # Dificultad
        'diff_easy': 'Fácil',
        'diff_medium': 'Media',
        'diff_hard': 'Difícil',
        
        # Lista de compra
        'shopping_list': 'Lista de la compra',
        'generate_list': '📝 Generar desde menú',
        'clear_list': '🗑️ Vaciar lista',
        'share_whatsapp': '📤 Compartir WhatsApp',
        'share_email': '📧 Enviar por email',
        'print_list': '🖨️ Imprimir',
        'estimated_cost': 'Coste estimado',
        'items_bought': 'comprados',
        'add_manual_item': '➕ Añadir producto manual',
        
        # Categorías supermercado
        'aisle_fruits': '🍎 Frutas y Verduras',
        'aisle_meat': '🥩 Carnicería',
        'aisle_fish': '🐟 Pescadería',
        'aisle_dairy': '🧀 Lácteos y Huevos',
        'aisle_bakery': '🍞 Panadería',
        'aisle_pantry': '🥫 Despensa',
        'aisle_frozen': '🧊 Congelados',
        'aisle_drinks': '🥤 Bebidas',
        'aisle_cleaning': '🧹 Limpieza',
        'aisle_other': '📦 Otros',
        
        # Familia
        'family_profile': 'Perfil familiar',
        'num_people': 'Número de personas',
        'adults': 'Adultos',
        'children': 'Niños',
        'weekly_budget': 'Presupuesto semanal',
        'allergies': 'Alergias e intolerancias',
        'preferences': 'Preferencias',
        'excluded_ingredients': 'Ingredientes excluidos',
        'save_profile': '💾 Guardar perfil',
        
        # Alergias
        'allergy_gluten': 'Gluten',
        'allergy_lactose': 'Lactosa',
        'allergy_nuts': 'Frutos secos',
        'allergy_eggs': 'Huevos',
        'allergy_fish': 'Pescado',
        'allergy_shellfish': 'Mariscos',
        'allergy_soy': 'Soja',
        
        # Preferencias
        'pref_no_pork': 'Sin cerdo',
        'pref_no_beef': 'Sin ternera',
        'pref_vegetarian': 'Vegetariano',
        'pref_vegan': 'Vegano',
        'pref_low_carb': 'Bajo en carbos',
        'pref_high_protein': 'Alto en proteína',
        'pref_quick_meals': 'Comidas rápidas',
        'pref_budget_friendly': 'Económico',
        
        # Asistente IA
        'ai_assistant': 'Asistente Inteligente',
        'ai_whats_in_fridge': '🧊 ¿Qué tengo en la nevera?',
        'ai_suggest_menu': '🎯 Sugiéreme un menú',
        'ai_healthier_option': '💚 Alternativa más saludable',
        'ai_cheaper_option': '💰 Alternativa más económica',
        'ai_faster_option': '⚡ Alternativa más rápida',
        'ai_placeholder': 'Escribe los ingredientes que tienes...',
        'ai_search': 'Buscar recetas',
        'ai_results': 'Recetas sugeridas',
        
        # Premium
        'premium_title': '⭐ FamFood Premium',
        'premium_subtitle': 'Desbloquea todo el potencial',
        'premium_feature_1': '✓ 500+ recetas exclusivas',
        'premium_feature_2': '✓ Asistente IA ilimitado',
        'premium_feature_3': '✓ Información nutricional completa',
        'premium_feature_4': '✓ Menús personalizados por IA',
        'premium_feature_5': '✓ Sin publicidad',
        'premium_price': '3,99€/mes',
        'premium_trial': 'Prueba 7 días gratis',
        
        # Unidades
        'min': 'min',
        'kcal': 'kcal',
        'g': 'g',
        'ml': 'ml',
        'unit': 'ud',
        'pinch': 'pizca',
        'tbsp': 'cda',
        'tsp': 'cdta',
        'cup': 'taza',
        
        # Otros
        'language': 'Idioma',
        'settings': 'Ajustes',
        'help': 'Ayuda',
        'about': 'Acerca de',
        'version': 'Versión',
        'loading': 'Cargando...',
        'no_results': 'No se encontraron resultados',
        'error': 'Error',
        'success': '¡Éxito!',
        'confirm': 'Confirmar',
        'cancel': 'Cancelar',
        'save': 'Guardar',
        'delete': 'Eliminar',
        'edit': 'Editar',
        'close': 'Cerrar',
    },
    'en': {
        # General
        'app_name': 'FamFood',
        'tagline': 'Your smart family meal planner',
        'welcome': 'Welcome to FamFood!',
        'welcome_text': 'Plan your family meals, save time and eat better.',
        
        # Navigation
        'nav_menu': '📅 Weekly Menu',
        'nav_recipes': '🍳 Recipes',
        'nav_shopping': '🛒 Shopping List',
        'nav_family': '👨‍👩‍👧‍👦 My Family',
        'nav_ai': '🤖 AI Assistant',
        'nav_favorites': '⭐ Favorites',
        
        # Weekly menu
        'week_of': 'Week of',
        'generate_menu': '🎲 Generate automatic menu',
        'clear_menu': '🗑️ Clear all',
        'copy_week': '📋 Copy previous week',
        'lunch': 'Lunch',
        'dinner': 'Dinner',
        'breakfast': 'Breakfast',
        'snack': 'Snack',
        'empty_slot': 'Tap to add',
        'change_recipe': '🔄 Change',
        'remove_recipe': '❌ Remove',
        
        # Days
        'monday': 'Monday', 'tuesday': 'Tuesday', 'wednesday': 'Wednesday',
        'thursday': 'Thursday', 'friday': 'Friday', 'saturday': 'Saturday', 'sunday': 'Sunday',
        'mon': 'Mon', 'tue': 'Tue', 'wed': 'Wed', 'thu': 'Thu', 'fri': 'Fri', 'sat': 'Sat', 'sun': 'Sun',
        
        # Recipes
        'search_recipes': 'Search recipes...',
        'all_categories': 'All',
        'filter_time': 'Max time',
        'filter_difficulty': 'Difficulty',
        'filter_calories': 'Max calories',
        'sort_by': 'Sort by',
        'sort_name': 'Name',
        'sort_time': 'Time',
        'sort_calories': 'Calories',
        'sort_rating': 'Rating',
        'prep_time': 'Prep time',
        'cook_time': 'Cook time',
        'total_time': 'Total time',
        'servings': 'Servings',
        'difficulty': 'Difficulty',
        'calories': 'Calories',
        'proteins': 'Proteins',
        'carbs': 'Carbohydrates',
        'fats': 'Fats',
        'fiber': 'Fiber',
        'ingredients': 'Ingredients',
        'instructions': 'Instructions',
        'tips': 'Tips',
        'nutrition_info': 'Nutrition info',
        'per_serving': 'Per serving',
        'add_to_menu': '➕ Add to menu',
        'add_to_favorites': '⭐ Add to favorites',
        'remove_from_favorites': '💔 Remove from favorites',
        'similar_recipes': 'Similar recipes',
        'view_recipe': 'View recipe',
        
        # Categories
        'cat_all': '🍽️ All',
        'cat_meat': '🥩 Meat',
        'cat_fish': '🐟 Fish',
        'cat_vegetarian': '🥬 Vegetarian',
        'cat_pasta': '🍝 Pasta',
        'cat_rice': '🍚 Rice',
        'cat_soup': '🍲 Soups & Stews',
        'cat_salad': '🥗 Salads',
        'cat_eggs': '🥚 Eggs',
        'cat_legumes': '🫘 Legumes',
        'cat_quick': '⚡ Quick (<20 min)',
        'cat_kids': '👶 Kid-friendly',
        'cat_healthy': '💚 Healthy',
        'cat_comfort': '🏠 Comfort food',
        'cat_international': '🌍 International',
        
        # Difficulty
        'diff_easy': 'Easy',
        'diff_medium': 'Medium',
        'diff_hard': 'Hard',
        
        # Shopping list
        'shopping_list': 'Shopping list',
        'generate_list': '📝 Generate from menu',
        'clear_list': '🗑️ Clear list',
        'share_whatsapp': '📤 Share WhatsApp',
        'share_email': '📧 Send by email',
        'print_list': '🖨️ Print',
        'estimated_cost': 'Estimated cost',
        'items_bought': 'bought',
        'add_manual_item': '➕ Add item manually',
        
        # Supermarket aisles
        'aisle_fruits': '🍎 Fruits & Vegetables',
        'aisle_meat': '🥩 Meat',
        'aisle_fish': '🐟 Fish',
        'aisle_dairy': '🧀 Dairy & Eggs',
        'aisle_bakery': '🍞 Bakery',
        'aisle_pantry': '🥫 Pantry',
        'aisle_frozen': '🧊 Frozen',
        'aisle_drinks': '🥤 Drinks',
        'aisle_cleaning': '🧹 Cleaning',
        'aisle_other': '📦 Other',
        
        # Family
        'family_profile': 'Family profile',
        'num_people': 'Number of people',
        'adults': 'Adults',
        'children': 'Children',
        'weekly_budget': 'Weekly budget',
        'allergies': 'Allergies & intolerances',
        'preferences': 'Preferences',
        'excluded_ingredients': 'Excluded ingredients',
        'save_profile': '💾 Save profile',
        
        # Allergies
        'allergy_gluten': 'Gluten',
        'allergy_lactose': 'Lactose',
        'allergy_nuts': 'Nuts',
        'allergy_eggs': 'Eggs',
        'allergy_fish': 'Fish',
        'allergy_shellfish': 'Shellfish',
        'allergy_soy': 'Soy',
        
        # Preferences
        'pref_no_pork': 'No pork',
        'pref_no_beef': 'No beef',
        'pref_vegetarian': 'Vegetarian',
        'pref_vegan': 'Vegan',
        'pref_low_carb': 'Low carb',
        'pref_high_protein': 'High protein',
        'pref_quick_meals': 'Quick meals',
        'pref_budget_friendly': 'Budget friendly',
        
        # AI Assistant
        'ai_assistant': 'Smart Assistant',
        'ai_whats_in_fridge': "🧊 What's in my fridge?",
        'ai_suggest_menu': '🎯 Suggest a menu',
        'ai_healthier_option': '💚 Healthier alternative',
        'ai_cheaper_option': '💰 Cheaper alternative',
        'ai_faster_option': '⚡ Faster alternative',
        'ai_placeholder': 'Type the ingredients you have...',
        'ai_search': 'Find recipes',
        'ai_results': 'Suggested recipes',
        
        # Premium
        'premium_title': '⭐ FamFood Premium',
        'premium_subtitle': 'Unlock full potential',
        'premium_feature_1': '✓ 500+ exclusive recipes',
        'premium_feature_2': '✓ Unlimited AI assistant',
        'premium_feature_3': '✓ Complete nutrition info',
        'premium_feature_4': '✓ AI-personalized menus',
        'premium_feature_5': '✓ Ad-free experience',
        'premium_price': '€3.99/month',
        'premium_trial': 'Try 7 days free',
        
        # Units
        'min': 'min',
        'kcal': 'kcal',
        'g': 'g',
        'ml': 'ml',
        'unit': 'pc',
        'pinch': 'pinch',
        'tbsp': 'tbsp',
        'tsp': 'tsp',
        'cup': 'cup',
        
        # Other
        'language': 'Language',
        'settings': 'Settings',
        'help': 'Help',
        'about': 'About',
        'version': 'Version',
        'loading': 'Loading...',
        'no_results': 'No results found',
        'error': 'Error',
        'success': 'Success!',
        'confirm': 'Confirm',
        'cancel': 'Cancel',
        'save': 'Save',
        'delete': 'Delete',
        'edit': 'Edit',
        'close': 'Close',
    },
    'fr': {
        # General
        'app_name': 'FamFood',
        'tagline': 'Votre planificateur de repas familial intelligent',
        'welcome': 'Bienvenue sur FamFood!',
        'welcome_text': 'Planifiez les repas de votre famille, gagnez du temps et mangez mieux.',
        
        # Navigation
        'nav_menu': '📅 Menu Hebdo',
        'nav_recipes': '🍳 Recettes',
        'nav_shopping': '🛒 Liste Courses',
        'nav_family': '👨‍👩‍👧‍👦 Ma Famille',
        'nav_ai': '🤖 Assistant IA',
        'nav_favorites': '⭐ Favoris',
        
        # Weekly menu
        'week_of': 'Semaine du',
        'generate_menu': '🎲 Générer menu automatique',
        'clear_menu': '🗑️ Tout effacer',
        'copy_week': '📋 Copier semaine précédente',
        'lunch': 'Déjeuner',
        'dinner': 'Dîner',
        'breakfast': 'Petit-déjeuner',
        'snack': 'Goûter',
        'empty_slot': 'Toucher pour ajouter',
        'change_recipe': '🔄 Changer',
        'remove_recipe': '❌ Supprimer',
        
        # Days
        'monday': 'Lundi', 'tuesday': 'Mardi', 'wednesday': 'Mercredi',
        'thursday': 'Jeudi', 'friday': 'Vendredi', 'saturday': 'Samedi', 'sunday': 'Dimanche',
        'mon': 'Lun', 'tue': 'Mar', 'wed': 'Mer', 'thu': 'Jeu', 'fri': 'Ven', 'sat': 'Sam', 'sun': 'Dim',
        
        # Recipes
        'search_recipes': 'Rechercher des recettes...',
        'all_categories': 'Toutes',
        'filter_time': 'Temps max',
        'filter_difficulty': 'Difficulté',
        'filter_calories': 'Calories max',
        'sort_by': 'Trier par',
        'sort_name': 'Nom',
        'sort_time': 'Temps',
        'sort_calories': 'Calories',
        'sort_rating': 'Note',
        'prep_time': 'Préparation',
        'cook_time': 'Cuisson',
        'total_time': 'Temps total',
        'servings': 'Portions',
        'difficulty': 'Difficulté',
        'calories': 'Calories',
        'proteins': 'Protéines',
        'carbs': 'Glucides',
        'fats': 'Lipides',
        'fiber': 'Fibres',
        'ingredients': 'Ingrédients',
        'instructions': 'Préparation',
        'tips': 'Conseils',
        'nutrition_info': 'Infos nutritionnelles',
        'per_serving': 'Par portion',
        'add_to_menu': '➕ Ajouter au menu',
        'add_to_favorites': '⭐ Ajouter aux favoris',
        'remove_from_favorites': '💔 Retirer des favoris',
        'similar_recipes': 'Recettes similaires',
        'view_recipe': 'Voir la recette',
        
        # Categories
        'cat_all': '🍽️ Toutes',
        'cat_meat': '🥩 Viandes',
        'cat_fish': '🐟 Poissons',
        'cat_vegetarian': '🥬 Végétarien',
        'cat_pasta': '🍝 Pâtes',
        'cat_rice': '🍚 Riz',
        'cat_soup': '🍲 Soupes et Potages',
        'cat_salad': '🥗 Salades',
        'cat_eggs': '🥚 Œufs',
        'cat_legumes': '🫘 Légumineuses',
        'cat_quick': '⚡ Rapides (<20 min)',
        'cat_kids': '👶 Pour enfants',
        'cat_healthy': '💚 Sain',
        'cat_comfort': '🏠 Réconfortant',
        'cat_international': '🌍 International',
        
        # Difficulty
        'diff_easy': 'Facile',
        'diff_medium': 'Moyen',
        'diff_hard': 'Difficile',
        
        # Shopping list
        'shopping_list': 'Liste de courses',
        'generate_list': '📝 Générer depuis le menu',
        'clear_list': '🗑️ Vider la liste',
        'share_whatsapp': '📤 Partager WhatsApp',
        'share_email': '📧 Envoyer par email',
        'print_list': '🖨️ Imprimer',
        'estimated_cost': 'Coût estimé',
        'items_bought': 'achetés',
        'add_manual_item': '➕ Ajouter un article',
        
        # Supermarket aisles
        'aisle_fruits': '🍎 Fruits et Légumes',
        'aisle_meat': '🥩 Boucherie',
        'aisle_fish': '🐟 Poissonnerie',
        'aisle_dairy': '🧀 Produits Laitiers',
        'aisle_bakery': '🍞 Boulangerie',
        'aisle_pantry': '🥫 Épicerie',
        'aisle_frozen': '🧊 Surgelés',
        'aisle_drinks': '🥤 Boissons',
        'aisle_cleaning': '🧹 Entretien',
        'aisle_other': '📦 Autres',
        
        # Family
        'family_profile': 'Profil familial',
        'num_people': 'Nombre de personnes',
        'adults': 'Adultes',
        'children': 'Enfants',
        'weekly_budget': 'Budget hebdomadaire',
        'allergies': 'Allergies et intolérances',
        'preferences': 'Préférences',
        'excluded_ingredients': 'Ingrédients exclus',
        'save_profile': '💾 Enregistrer le profil',
        
        # Allergies
        'allergy_gluten': 'Gluten',
        'allergy_lactose': 'Lactose',
        'allergy_nuts': 'Fruits à coque',
        'allergy_eggs': 'Œufs',
        'allergy_fish': 'Poisson',
        'allergy_shellfish': 'Fruits de mer',
        'allergy_soy': 'Soja',
        
        # Preferences
        'pref_no_pork': 'Sans porc',
        'pref_no_beef': 'Sans bœuf',
        'pref_vegetarian': 'Végétarien',
        'pref_vegan': 'Végan',
        'pref_low_carb': 'Faible en glucides',
        'pref_high_protein': 'Riche en protéines',
        'pref_quick_meals': 'Repas rapides',
        'pref_budget_friendly': 'Économique',
        
        # AI Assistant
        'ai_assistant': 'Assistant Intelligent',
        'ai_whats_in_fridge': "🧊 Qu'est-ce que j'ai dans mon frigo?",
        'ai_suggest_menu': '🎯 Suggère-moi un menu',
        'ai_healthier_option': '💚 Alternative plus saine',
        'ai_cheaper_option': '💰 Alternative moins chère',
        'ai_faster_option': '⚡ Alternative plus rapide',
        'ai_placeholder': 'Écrivez les ingrédients que vous avez...',
        'ai_search': 'Trouver des recettes',
        'ai_results': 'Recettes suggérées',
        
        # Premium
        'premium_title': '⭐ FamFood Premium',
        'premium_subtitle': 'Débloquez tout le potentiel',
        'premium_feature_1': '✓ 500+ recettes exclusives',
        'premium_feature_2': '✓ Assistant IA illimité',
        'premium_feature_3': '✓ Infos nutritionnelles complètes',
        'premium_feature_4': '✓ Menus personnalisés par IA',
        'premium_feature_5': '✓ Sans publicité',
        'premium_price': '3,99€/mois',
        'premium_trial': 'Essayez 7 jours gratuits',
        
        # Units
        'min': 'min',
        'kcal': 'kcal',
        'g': 'g',
        'ml': 'ml',
        'unit': 'pce',
        'pinch': 'pincée',
        'tbsp': 'c.s.',
        'tsp': 'c.c.',
        'cup': 'tasse',
        
        # Other
        'language': 'Langue',
        'settings': 'Paramètres',
        'help': 'Aide',
        'about': 'À propos',
        'version': 'Version',
        'loading': 'Chargement...',
        'no_results': 'Aucun résultat trouvé',
        'error': 'Erreur',
        'success': 'Succès!',
        'confirm': 'Confirmer',
        'cancel': 'Annuler',
        'save': 'Enregistrer',
        'delete': 'Supprimer',
        'edit': 'Modifier',
        'close': 'Fermer',
    },
    'de': {
        # General
        'app_name': 'FamFood',
        'tagline': 'Ihr intelligenter Familien-Menüplaner',
        'welcome': 'Willkommen bei FamFood!',
        'welcome_text': 'Planen Sie die Mahlzeiten Ihrer Familie, sparen Sie Zeit und essen Sie besser.',
        
        # Navigation
        'nav_menu': '📅 Wochenmenü',
        'nav_recipes': '🍳 Rezepte',
        'nav_shopping': '🛒 Einkaufsliste',
        'nav_family': '👨‍👩‍👧‍👦 Meine Familie',
        'nav_ai': '🤖 KI-Assistent',
        'nav_favorites': '⭐ Favoriten',
        
        # Weekly menu
        'week_of': 'Woche vom',
        'generate_menu': '🎲 Automatisches Menü erstellen',
        'clear_menu': '🗑️ Alles löschen',
        'copy_week': '📋 Vorherige Woche kopieren',
        'lunch': 'Mittagessen',
        'dinner': 'Abendessen',
        'breakfast': 'Frühstück',
        'snack': 'Snack',
        'empty_slot': 'Tippen zum Hinzufügen',
        'change_recipe': '🔄 Ändern',
        'remove_recipe': '❌ Entfernen',
        
        # Days
        'monday': 'Montag', 'tuesday': 'Dienstag', 'wednesday': 'Mittwoch',
        'thursday': 'Donnerstag', 'friday': 'Freitag', 'saturday': 'Samstag', 'sunday': 'Sonntag',
        'mon': 'Mo', 'tue': 'Di', 'wed': 'Mi', 'thu': 'Do', 'fri': 'Fr', 'sat': 'Sa', 'sun': 'So',
        
        # Recipes
        'search_recipes': 'Rezepte suchen...',
        'all_categories': 'Alle',
        'filter_time': 'Max. Zeit',
        'filter_difficulty': 'Schwierigkeit',
        'filter_calories': 'Max. Kalorien',
        'sort_by': 'Sortieren nach',
        'sort_name': 'Name',
        'sort_time': 'Zeit',
        'sort_calories': 'Kalorien',
        'sort_rating': 'Bewertung',
        'prep_time': 'Vorbereitung',
        'cook_time': 'Kochzeit',
        'total_time': 'Gesamtzeit',
        'servings': 'Portionen',
        'difficulty': 'Schwierigkeit',
        'calories': 'Kalorien',
        'proteins': 'Proteine',
        'carbs': 'Kohlenhydrate',
        'fats': 'Fette',
        'fiber': 'Ballaststoffe',
        'ingredients': 'Zutaten',
        'instructions': 'Zubereitung',
        'tips': 'Tipps',
        'nutrition_info': 'Nährwertangaben',
        'per_serving': 'Pro Portion',
        'add_to_menu': '➕ Zum Menü hinzufügen',
        'add_to_favorites': '⭐ Zu Favoriten hinzufügen',
        'remove_from_favorites': '💔 Aus Favoriten entfernen',
        'similar_recipes': 'Ähnliche Rezepte',
        'view_recipe': 'Rezept ansehen',
        
        # Categories
        'cat_all': '🍽️ Alle',
        'cat_meat': '🥩 Fleisch',
        'cat_fish': '🐟 Fisch',
        'cat_vegetarian': '🥬 Vegetarisch',
        'cat_pasta': '🍝 Pasta',
        'cat_rice': '🍚 Reis',
        'cat_soup': '🍲 Suppen & Eintöpfe',
        'cat_salad': '🥗 Salate',
        'cat_eggs': '🥚 Eier',
        'cat_legumes': '🫘 Hülsenfrüchte',
        'cat_quick': '⚡ Schnell (<20 Min)',
        'cat_kids': '👶 Kinderfreundlich',
        'cat_healthy': '💚 Gesund',
        'cat_comfort': '🏠 Comfort Food',
        'cat_international': '🌍 International',
        
        # Difficulty
        'diff_easy': 'Einfach',
        'diff_medium': 'Mittel',
        'diff_hard': 'Schwer',
        
        # Shopping list
        'shopping_list': 'Einkaufsliste',
        'generate_list': '📝 Aus Menü erstellen',
        'clear_list': '🗑️ Liste leeren',
        'share_whatsapp': '📤 WhatsApp teilen',
        'share_email': '📧 Per E-Mail senden',
        'print_list': '🖨️ Drucken',
        'estimated_cost': 'Geschätzte Kosten',
        'items_bought': 'gekauft',
        'add_manual_item': '➕ Artikel hinzufügen',
        
        # Supermarket aisles
        'aisle_fruits': '🍎 Obst & Gemüse',
        'aisle_meat': '🥩 Fleisch',
        'aisle_fish': '🐟 Fisch',
        'aisle_dairy': '🧀 Milchprodukte',
        'aisle_bakery': '🍞 Bäckerei',
        'aisle_pantry': '🥫 Vorratskammer',
        'aisle_frozen': '🧊 Tiefkühl',
        'aisle_drinks': '🥤 Getränke',
        'aisle_cleaning': '🧹 Reinigung',
        'aisle_other': '📦 Sonstiges',
        
        # Family
        'family_profile': 'Familienprofil',
        'num_people': 'Anzahl Personen',
        'adults': 'Erwachsene',
        'children': 'Kinder',
        'weekly_budget': 'Wochenbudget',
        'allergies': 'Allergien & Unverträglichkeiten',
        'preferences': 'Vorlieben',
        'excluded_ingredients': 'Ausgeschlossene Zutaten',
        'save_profile': '💾 Profil speichern',
        
        # Allergies
        'allergy_gluten': 'Gluten',
        'allergy_lactose': 'Laktose',
        'allergy_nuts': 'Nüsse',
        'allergy_eggs': 'Eier',
        'allergy_fish': 'Fisch',
        'allergy_shellfish': 'Meeresfrüchte',
        'allergy_soy': 'Soja',
        
        # Preferences
        'pref_no_pork': 'Kein Schweinefleisch',
        'pref_no_beef': 'Kein Rindfleisch',
        'pref_vegetarian': 'Vegetarisch',
        'pref_vegan': 'Vegan',
        'pref_low_carb': 'Low Carb',
        'pref_high_protein': 'Proteinreich',
        'pref_quick_meals': 'Schnelle Gerichte',
        'pref_budget_friendly': 'Preiswert',
        
        # AI Assistant
        'ai_assistant': 'Intelligenter Assistent',
        'ai_whats_in_fridge': '🧊 Was habe ich im Kühlschrank?',
        'ai_suggest_menu': '🎯 Menü vorschlagen',
        'ai_healthier_option': '💚 Gesündere Alternative',
        'ai_cheaper_option': '💰 Günstigere Alternative',
        'ai_faster_option': '⚡ Schnellere Alternative',
        'ai_placeholder': 'Schreiben Sie die Zutaten, die Sie haben...',
        'ai_search': 'Rezepte finden',
        'ai_results': 'Vorgeschlagene Rezepte',
        
        # Premium
        'premium_title': '⭐ FamFood Premium',
        'premium_subtitle': 'Volles Potenzial freischalten',
        'premium_feature_1': '✓ 500+ exklusive Rezepte',
        'premium_feature_2': '✓ Unbegrenzter KI-Assistent',
        'premium_feature_3': '✓ Vollständige Nährwertinfos',
        'premium_feature_4': '✓ KI-personalisierte Menüs',
        'premium_feature_5': '✓ Werbefrei',
        'premium_price': '3,99€/Monat',
        'premium_trial': '7 Tage kostenlos testen',
        
        # Units
        'min': 'Min',
        'kcal': 'kcal',
        'g': 'g',
        'ml': 'ml',
        'unit': 'Stk',
        'pinch': 'Prise',
        'tbsp': 'EL',
        'tsp': 'TL',
        'cup': 'Tasse',
        
        # Other
        'language': 'Sprache',
        'settings': 'Einstellungen',
        'help': 'Hilfe',
        'about': 'Über',
        'version': 'Version',
        'loading': 'Laden...',
        'no_results': 'Keine Ergebnisse gefunden',
        'error': 'Fehler',
        'success': 'Erfolg!',
        'confirm': 'Bestätigen',
        'cancel': 'Abbrechen',
        'save': 'Speichern',
        'delete': 'Löschen',
        'edit': 'Bearbeiten',
        'close': 'Schließen',
    }
}

# =====================================================
# BASE DE DATOS DE RECETAS - 100+ RECETAS TRADUCIDAS
# =====================================================

RECIPES_DB = [
    # =============== RECETAS ESPAÑOLAS ===============
    {
        'id': 'es001',
        'name': {'es': 'Tortilla Española', 'en': 'Spanish Omelette', 'fr': 'Omelette Espagnole', 'de': 'Spanisches Omelett'},
        'category': 'eggs',
        'image': '🥚',
        'time': 35,
        'difficulty': 'easy',
        'servings': 4,
        'calories': 250,
        'proteins': 12,
        'carbs': 22,
        'fats': 14,
        'fiber': 2,
        'cost': 4.50,
        'ingredients': {
            'es': ['6 huevos', '4 patatas medianas (600g)', '1 cebolla grande', '100ml aceite de oliva', 'Sal al gusto'],
            'en': ['6 eggs', '4 medium potatoes (600g)', '1 large onion', '100ml olive oil', 'Salt to taste'],
            'fr': ['6 œufs', '4 pommes de terre moyennes (600g)', '1 gros oignon', '100ml huile d\'olive', 'Sel à goût'],
            'de': ['6 Eier', '4 mittelgroße Kartoffeln (600g)', '1 große Zwiebel', '100ml Olivenöl', 'Salz nach Geschmack']
        },
        'instructions': {
            'es': '1. Pelar y cortar las patatas en rodajas finas. Picar la cebolla.\n2. Calentar el aceite y freír las patatas con la cebolla a fuego lento 20 min.\n3. Batir los huevos con sal. Escurrir las patatas y mezclar con el huevo.\n4. Cuajar en sartén 3 min por cada lado. Dar la vuelta con un plato.',
            'en': '1. Peel and slice the potatoes thinly. Chop the onion.\n2. Heat the oil and fry potatoes with onion over low heat for 20 min.\n3. Beat the eggs with salt. Drain potatoes and mix with egg.\n4. Cook in pan 3 min each side. Flip using a plate.',
            'fr': '1. Éplucher et couper les pommes de terre en fines tranches. Émincer l\'oignon.\n2. Chauffer l\'huile et faire frire les pommes de terre avec l\'oignon à feu doux 20 min.\n3. Battre les œufs avec du sel. Égoutter les pommes de terre et mélanger avec l\'œuf.\n4. Cuire dans la poêle 3 min de chaque côté. Retourner avec une assiette.',
            'de': '1. Kartoffeln schälen und in dünne Scheiben schneiden. Zwiebel hacken.\n2. Öl erhitzen und Kartoffeln mit Zwiebel bei niedriger Hitze 20 Min braten.\n3. Eier mit Salz verquirlen. Kartoffeln abtropfen und mit Ei mischen.\n4. In der Pfanne 3 Min pro Seite garen. Mit einem Teller wenden.'
        },
        'tips': {
            'es': 'Para una tortilla más jugosa, déjala poco hecha por dentro.',
            'en': 'For a juicier omelette, leave it slightly runny inside.',
            'fr': 'Pour une omelette plus juteuse, laissez-la baveuse à l\'intérieur.',
            'de': 'Für ein saftigeres Omelett innen leicht flüssig lassen.'
        },
        'tags': ['spanish', 'eggs', 'vegetarian', 'comfort', 'kids']
    },
    {
        'id': 'es002',
        'name': {'es': 'Paella de Pollo', 'en': 'Chicken Paella', 'fr': 'Paella au Poulet', 'de': 'Hähnchen-Paella'},
        'category': 'rice',
        'image': '🥘',
        'time': 55,
        'difficulty': 'medium',
        'servings': 6,
        'calories': 420,
        'proteins': 28,
        'carbs': 45,
        'fats': 15,
        'fiber': 3,
        'cost': 12.00,
        'ingredients': {
            'es': ['400g arroz bomba', '600g pollo troceado', '200g judías verdes', '1 tomate rallado', '1 cucharadita de pimentón', 'Azafrán', '1.2L caldo de pollo', 'Aceite de oliva', 'Sal'],
            'en': ['400g bomba rice', '600g chicken pieces', '200g green beans', '1 grated tomato', '1 tsp paprika', 'Saffron', '1.2L chicken broth', 'Olive oil', 'Salt'],
            'fr': ['400g riz bomba', '600g morceaux de poulet', '200g haricots verts', '1 tomate râpée', '1 c.c. de paprika', 'Safran', '1.2L bouillon de poulet', 'Huile d\'olive', 'Sel'],
            'de': ['400g Bomba-Reis', '600g Hähnchenteile', '200g grüne Bohnen', '1 geriebene Tomate', '1 TL Paprika', 'Safran', '1.2L Hühnerbrühe', 'Olivenöl', 'Salz']
        },
        'instructions': {
            'es': '1. Dorar el pollo en la paella con aceite. Reservar.\n2. Sofreír las judías 5 min. Añadir tomate y pimentón.\n3. Agregar el caldo caliente y el azafrán. Hervir 5 min.\n4. Añadir el arroz repartido. Colocar el pollo encima.\n5. Cocer 18-20 min sin remover. Dejar reposar 5 min.',
            'en': '1. Brown the chicken in the pan with oil. Set aside.\n2. Sauté green beans 5 min. Add tomato and paprika.\n3. Add hot broth and saffron. Boil 5 min.\n4. Add rice evenly distributed. Place chicken on top.\n5. Cook 18-20 min without stirring. Rest 5 min.',
            'fr': '1. Dorer le poulet dans la poêle avec de l\'huile. Réserver.\n2. Faire sauter les haricots 5 min. Ajouter tomate et paprika.\n3. Ajouter le bouillon chaud et le safran. Bouillir 5 min.\n4. Ajouter le riz bien réparti. Placer le poulet dessus.\n5. Cuire 18-20 min sans remuer. Laisser reposer 5 min.',
            'de': '1. Hähnchen in der Pfanne mit Öl anbraten. Beiseite stellen.\n2. Bohnen 5 Min anbraten. Tomate und Paprika hinzufügen.\n3. Heiße Brühe und Safran hinzufügen. 5 Min kochen.\n4. Reis gleichmäßig verteilen. Hähnchen oben platzieren.\n5. 18-20 Min kochen ohne umzurühren. 5 Min ruhen lassen.'
        },
        'tips': {
            'es': 'El socarrat (arroz tostado del fondo) es la parte más deseada.',
            'en': 'The socarrat (crispy bottom rice) is the most desired part.',
            'fr': 'Le socarrat (riz croustillant du fond) est la partie la plus recherchée.',
            'de': 'Der Socarrat (knuspriger Bodenreis) ist der begehrteste Teil.'
        },
        'tags': ['spanish', 'rice', 'meat', 'traditional']
    },
    {
        'id': 'es003',
        'name': {'es': 'Gazpacho Andaluz', 'en': 'Andalusian Gazpacho', 'fr': 'Gazpacho Andalou', 'de': 'Andalusischer Gazpacho'},
        'category': 'soup',
        'image': '🍅',
        'time': 15,
        'difficulty': 'easy',
        'servings': 4,
        'calories': 120,
        'proteins': 3,
        'carbs': 12,
        'fats': 7,
        'fiber': 3,
        'cost': 4.00,
        'ingredients': {
            'es': ['1kg tomates maduros', '1 pepino', '1 pimiento verde', '1 diente de ajo', '50ml vinagre de Jerez', '100ml aceite de oliva', 'Sal', 'Agua fría'],
            'en': ['1kg ripe tomatoes', '1 cucumber', '1 green pepper', '1 garlic clove', '50ml sherry vinegar', '100ml olive oil', 'Salt', 'Cold water'],
            'fr': ['1kg tomates mûres', '1 concombre', '1 poivron vert', '1 gousse d\'ail', '50ml vinaigre de Xérès', '100ml huile d\'olive', 'Sel', 'Eau froide'],
            'de': ['1kg reife Tomaten', '1 Gurke', '1 grüne Paprika', '1 Knoblauchzehe', '50ml Sherry-Essig', '100ml Olivenöl', 'Salz', 'Kaltes Wasser']
        },
        'instructions': {
            'es': '1. Lavar y trocear todas las verduras.\n2. Poner en la batidora con el ajo, vinagre y sal.\n3. Triturar hasta obtener una textura fina.\n4. Añadir el aceite en hilo mientras se bate.\n5. Ajustar la consistencia con agua fría. Refrigerar 2h.',
            'en': '1. Wash and chop all vegetables.\n2. Put in blender with garlic, vinegar and salt.\n3. Blend until smooth texture.\n4. Add oil in a stream while blending.\n5. Adjust consistency with cold water. Refrigerate 2h.',
            'fr': '1. Laver et couper tous les légumes.\n2. Mettre dans le mixeur avec l\'ail, le vinaigre et le sel.\n3. Mixer jusqu\'à obtenir une texture lisse.\n4. Ajouter l\'huile en filet tout en mixant.\n5. Ajuster la consistance avec de l\'eau froide. Réfrigérer 2h.',
            'de': '1. Alle Gemüse waschen und zerkleinern.\n2. Mit Knoblauch, Essig und Salz in den Mixer geben.\n3. Zu einer feinen Textur pürieren.\n4. Öl im Strahl beim Mixen hinzufügen.\n5. Konsistenz mit kaltem Wasser anpassen. 2 Std. kühlen.'
        },
        'tips': {
            'es': 'Servir muy frío con tropezones de verdura picada.',
            'en': 'Serve very cold with diced vegetable toppings.',
            'fr': 'Servir très froid avec des légumes en dés.',
            'de': 'Sehr kalt servieren mit gewürfeltem Gemüse als Topping.'
        },
        'tags': ['spanish', 'soup', 'vegetarian', 'healthy', 'quick', 'summer']
    },
    {
        'id': 'es004',
        'name': {'es': 'Lentejas Estofadas', 'en': 'Stewed Lentils', 'fr': 'Lentilles en Ragoût', 'de': 'Geschmorte Linsen'},
        'category': 'legumes',
        'image': '🍲',
        'time': 50,
        'difficulty': 'easy',
        'servings': 6,
        'calories': 320,
        'proteins': 18,
        'carbs': 42,
        'fats': 8,
        'fiber': 12,
        'cost': 5.00,
        'ingredients': {
            'es': ['400g lentejas', '1 chorizo', '100g panceta', '2 zanahorias', '1 cebolla', '2 patatas', '2 hojas de laurel', 'Pimentón', 'Aceite', 'Sal'],
            'en': ['400g lentils', '1 chorizo', '100g bacon', '2 carrots', '1 onion', '2 potatoes', '2 bay leaves', 'Paprika', 'Oil', 'Salt'],
            'fr': ['400g lentilles', '1 chorizo', '100g lardons', '2 carottes', '1 oignon', '2 pommes de terre', '2 feuilles de laurier', 'Paprika', 'Huile', 'Sel'],
            'de': ['400g Linsen', '1 Chorizo', '100g Speck', '2 Karotten', '1 Zwiebel', '2 Kartoffeln', '2 Lorbeerblätter', 'Paprika', 'Öl', 'Salz']
        },
        'instructions': {
            'es': '1. Poner las lentejas en una olla con agua fría y el laurel.\n2. Añadir las zanahorias y patatas troceadas.\n3. Sofreír la cebolla con la panceta. Añadir pimentón.\n4. Incorporar el sofrito y el chorizo a las lentejas.\n5. Cocer a fuego lento 45 min. Salar al final.',
            'en': '1. Put lentils in a pot with cold water and bay leaves.\n2. Add chopped carrots and potatoes.\n3. Sauté onion with bacon. Add paprika.\n4. Add the sauté and chorizo to the lentils.\n5. Simmer for 45 min. Salt at the end.',
            'fr': '1. Mettre les lentilles dans une marmite avec de l\'eau froide et le laurier.\n2. Ajouter les carottes et pommes de terre coupées.\n3. Faire revenir l\'oignon avec les lardons. Ajouter le paprika.\n4. Incorporer le sauté et le chorizo aux lentilles.\n5. Mijoter 45 min. Saler à la fin.',
            'de': '1. Linsen in einen Topf mit kaltem Wasser und Lorbeer geben.\n2. Geschnittene Karotten und Kartoffeln hinzufügen.\n3. Zwiebel mit Speck anbraten. Paprika hinzufügen.\n4. Bratzutaten und Chorizo zu den Linsen geben.\n5. 45 Min köcheln lassen. Am Ende salzen.'
        },
        'tips': {
            'es': 'Están más ricas de un día para otro.',
            'en': 'They taste even better the next day.',
            'fr': 'Elles sont encore meilleures le lendemain.',
            'de': 'Sie schmecken am nächsten Tag noch besser.'
        },
        'tags': ['spanish', 'legumes', 'meat', 'comfort', 'winter', 'budget']
    },
    
    # =============== RECETAS ITALIANAS/INTERNACIONALES ===============
    {
        'id': 'it001',
        'name': {'es': 'Espaguetis Carbonara', 'en': 'Spaghetti Carbonara', 'fr': 'Spaghetti Carbonara', 'de': 'Spaghetti Carbonara'},
        'category': 'pasta',
        'image': '🍝',
        'time': 25,
        'difficulty': 'easy',
        'servings': 4,
        'calories': 480,
        'proteins': 22,
        'carbs': 52,
        'fats': 20,
        'fiber': 2,
        'cost': 6.00,
        'ingredients': {
            'es': ['400g espaguetis', '200g guanciale o panceta', '4 yemas de huevo', '100g pecorino rallado', 'Pimienta negra', 'Sal'],
            'en': ['400g spaghetti', '200g guanciale or pancetta', '4 egg yolks', '100g grated pecorino', 'Black pepper', 'Salt'],
            'fr': ['400g spaghetti', '200g guanciale ou pancetta', '4 jaunes d\'œufs', '100g pecorino râpé', 'Poivre noir', 'Sel'],
            'de': ['400g Spaghetti', '200g Guanciale oder Pancetta', '4 Eigelb', '100g geriebener Pecorino', 'Schwarzer Pfeffer', 'Salz']
        },
        'instructions': {
            'es': '1. Cocer la pasta en agua con sal.\n2. Dorar el guanciale en una sartén sin aceite.\n3. Mezclar yemas, pecorino y pimienta en un bol.\n4. Escurrir la pasta reservando un poco de agua.\n5. Mezclar todo fuera del fuego para no cuajar el huevo.',
            'en': '1. Cook pasta in salted water.\n2. Brown guanciale in a pan without oil.\n3. Mix yolks, pecorino and pepper in a bowl.\n4. Drain pasta reserving some water.\n5. Mix everything off heat to prevent egg from scrambling.',
            'fr': '1. Cuire les pâtes dans l\'eau salée.\n2. Dorer le guanciale dans une poêle sans huile.\n3. Mélanger les jaunes, le pecorino et le poivre dans un bol.\n4. Égoutter les pâtes en réservant un peu d\'eau.\n5. Mélanger le tout hors du feu pour ne pas cuire l\'œuf.',
            'de': '1. Pasta in Salzwasser kochen.\n2. Guanciale in einer Pfanne ohne Öl anbraten.\n3. Eigelb, Pecorino und Pfeffer in einer Schüssel mischen.\n4. Pasta abgießen, etwas Wasser aufheben.\n5. Alles vom Herd nehmen und mischen, damit das Ei nicht stockt.'
        },
        'tips': {
            'es': 'La clave es mezclar fuera del fuego para una salsa cremosa.',
            'en': 'The key is mixing off heat for a creamy sauce.',
            'fr': 'La clé est de mélanger hors du feu pour une sauce crémeuse.',
            'de': 'Der Schlüssel ist das Mischen vom Herd für eine cremige Sauce.'
        },
        'tags': ['italian', 'pasta', 'meat', 'quick', 'comfort']
    },
    {
        'id': 'it002',
        'name': {'es': 'Lasaña Boloñesa', 'en': 'Bolognese Lasagna', 'fr': 'Lasagnes Bolognaise', 'de': 'Lasagne Bolognese'},
        'category': 'pasta',
        'image': '🍝',
        'time': 90,
        'difficulty': 'medium',
        'servings': 8,
        'calories': 520,
        'proteins': 28,
        'carbs': 42,
        'fats': 26,
        'fiber': 3,
        'cost': 14.00,
        'ingredients': {
            'es': ['12 láminas de lasaña', '500g carne picada mixta', '400g tomate triturado', '1 cebolla', '2 zanahorias', 'Vino tinto', 'Bechamel: 50g mantequilla, 50g harina, 500ml leche', '100g queso rallado'],
            'en': ['12 lasagna sheets', '500g mixed ground meat', '400g crushed tomatoes', '1 onion', '2 carrots', 'Red wine', 'Bechamel: 50g butter, 50g flour, 500ml milk', '100g grated cheese'],
            'fr': ['12 feuilles de lasagne', '500g viande hachée mixte', '400g tomates concassées', '1 oignon', '2 carottes', 'Vin rouge', 'Béchamel: 50g beurre, 50g farine, 500ml lait', '100g fromage râpé'],
            'de': ['12 Lasagneplatten', '500g gemischtes Hackfleisch', '400g passierte Tomaten', '1 Zwiebel', '2 Karotten', 'Rotwein', 'Bechamel: 50g Butter, 50g Mehl, 500ml Milch', '100g geriebener Käse']
        },
        'instructions': {
            'es': '1. Sofreír cebolla y zanahoria picadas. Añadir carne y dorar.\n2. Verter vino y dejar evaporar. Añadir tomate y cocer 30 min.\n3. Preparar bechamel: derretir mantequilla, añadir harina, verter leche sin dejar de remover.\n4. Montar: capa de boloñesa, lámina, bechamel. Repetir.\n5. Terminar con bechamel y queso. Hornear 40 min a 180°C.',
            'en': '1. Sauté chopped onion and carrot. Add meat and brown.\n2. Pour wine and let evaporate. Add tomatoes and cook 30 min.\n3. Make bechamel: melt butter, add flour, pour milk while stirring.\n4. Layer: bolognese, pasta sheet, bechamel. Repeat.\n5. Finish with bechamel and cheese. Bake 40 min at 180°C.',
            'fr': '1. Faire revenir l\'oignon et la carotte émincés. Ajouter la viande et dorer.\n2. Verser le vin et laisser évaporer. Ajouter les tomates et cuire 30 min.\n3. Préparer la béchamel: fondre le beurre, ajouter la farine, verser le lait en remuant.\n4. Monter: couche de bolognaise, feuille, béchamel. Répéter.\n5. Terminer avec béchamel et fromage. Cuire 40 min à 180°C.',
            'de': '1. Gehackte Zwiebel und Karotte anbraten. Fleisch hinzufügen und anbraten.\n2. Wein hinzufügen und verdampfen lassen. Tomaten hinzufügen und 30 Min kochen.\n3. Bechamel zubereiten: Butter schmelzen, Mehl hinzufügen, Milch unter Rühren hinzufügen.\n4. Schichten: Bolognese, Nudelplatte, Bechamel. Wiederholen.\n5. Mit Bechamel und Käse abschließen. 40 Min bei 180°C backen.'
        },
        'tips': {
            'es': 'Dejar reposar 10 minutos antes de cortar para que asiente.',
            'en': 'Let rest 10 minutes before cutting so it sets.',
            'fr': 'Laisser reposer 10 minutes avant de couper pour qu\'elle se tienne.',
            'de': '10 Minuten ruhen lassen vor dem Schneiden, damit sie fest wird.'
        },
        'tags': ['italian', 'pasta', 'meat', 'comfort', 'kids', 'family']
    },
    
    # =============== RECETAS BRITÁNICAS ===============
    {
        'id': 'uk001',
        'name': {'es': 'Shepherd\'s Pie', 'en': 'Shepherd\'s Pie', 'fr': 'Hachis Parmentier', 'de': 'Shepherd\'s Pie'},
        'category': 'meat',
        'image': '🥧',
        'time': 70,
        'difficulty': 'medium',
        'servings': 6,
        'calories': 450,
        'proteins': 25,
        'carbs': 38,
        'fats': 22,
        'fiber': 5,
        'cost': 10.00,
        'ingredients': {
            'es': ['500g carne de cordero picada', '1kg patatas', '2 zanahorias', '1 cebolla', '100g guisantes', '200ml caldo de carne', '2 cdas salsa Worcestershire', '100g mantequilla', '100ml leche', 'Romero', 'Sal y pimienta'],
            'en': ['500g minced lamb', '1kg potatoes', '2 carrots', '1 onion', '100g peas', '200ml beef stock', '2 tbsp Worcestershire sauce', '100g butter', '100ml milk', 'Rosemary', 'Salt and pepper'],
            'fr': ['500g agneau haché', '1kg pommes de terre', '2 carottes', '1 oignon', '100g petits pois', '200ml bouillon de bœuf', '2 c.s. sauce Worcestershire', '100g beurre', '100ml lait', 'Romarin', 'Sel et poivre'],
            'de': ['500g Lammhackfleisch', '1kg Kartoffeln', '2 Karotten', '1 Zwiebel', '100g Erbsen', '200ml Rinderbrühe', '2 EL Worcestershire-Sauce', '100g Butter', '100ml Milch', 'Rosmarin', 'Salz und Pfeffer']
        },
        'instructions': {
            'es': '1. Cocer las patatas, escurrir y hacer puré con mantequilla y leche.\n2. Sofreír cebolla y zanahoria. Añadir cordero y dorar.\n3. Agregar caldo, Worcestershire y romero. Cocer 15 min.\n4. Añadir guisantes. Poner en fuente de horno.\n5. Cubrir con puré, marcar con tenedor. Hornear 25 min a 200°C.',
            'en': '1. Boil potatoes, drain and mash with butter and milk.\n2. Sauté onion and carrot. Add lamb and brown.\n3. Add stock, Worcestershire and rosemary. Cook 15 min.\n4. Add peas. Put in baking dish.\n5. Top with mash, mark with fork. Bake 25 min at 200°C.',
            'fr': '1. Cuire les pommes de terre, égoutter et réduire en purée avec beurre et lait.\n2. Faire revenir oignon et carotte. Ajouter l\'agneau et dorer.\n3. Ajouter bouillon, Worcestershire et romarin. Cuire 15 min.\n4. Ajouter les petits pois. Mettre dans un plat allant au four.\n5. Couvrir de purée, marquer à la fourchette. Cuire 25 min à 200°C.',
            'de': '1. Kartoffeln kochen, abgießen und mit Butter und Milch pürieren.\n2. Zwiebel und Karotte anbraten. Lamm hinzufügen und anbraten.\n3. Brühe, Worcestershire und Rosmarin hinzufügen. 15 Min kochen.\n4. Erbsen hinzufügen. In Auflaufform geben.\n5. Mit Püree bedecken, mit Gabel Muster machen. 25 Min bei 200°C backen.'
        },
        'tips': {
            'es': 'Para gratinar mejor, añadir un poco de queso al puré.',
            'en': 'For better browning, add a little cheese to the mash.',
            'fr': 'Pour mieux gratiner, ajouter un peu de fromage à la purée.',
            'de': 'Für bessere Bräunung etwas Käse zum Püree geben.'
        },
        'tags': ['british', 'meat', 'comfort', 'winter', 'family']
    },
    {
        'id': 'uk002',
        'name': {'es': 'Fish and Chips', 'en': 'Fish and Chips', 'fr': 'Fish and Chips', 'de': 'Fish and Chips'},
        'category': 'fish',
        'image': '🐟',
        'time': 45,
        'difficulty': 'medium',
        'servings': 4,
        'calories': 680,
        'proteins': 32,
        'carbs': 65,
        'fats': 32,
        'fiber': 4,
        'cost': 12.00,
        'ingredients': {
            'es': ['4 filetes de bacalao (600g)', '1kg patatas', '200g harina', '250ml cerveza fría', '1 huevo', 'Aceite para freír', 'Guisantes (opcional)', 'Sal'],
            'en': ['4 cod fillets (600g)', '1kg potatoes', '200g flour', '250ml cold beer', '1 egg', 'Oil for frying', 'Peas (optional)', 'Salt'],
            'fr': ['4 filets de cabillaud (600g)', '1kg pommes de terre', '200g farine', '250ml bière froide', '1 œuf', 'Huile pour friture', 'Petits pois (optionnel)', 'Sel'],
            'de': ['4 Kabeljaufilets (600g)', '1kg Kartoffeln', '200g Mehl', '250ml kaltes Bier', '1 Ei', 'Öl zum Frittieren', 'Erbsen (optional)', 'Salz']
        },
        'instructions': {
            'es': '1. Cortar las patatas en bastones gruesos. Secar bien.\n2. Freír las patatas dos veces: primero a 130°C, luego a 180°C.\n3. Hacer la masa: mezclar harina, huevo, cerveza y sal.\n4. Pasar el pescado por harina, luego por la masa.\n5. Freír el pescado a 180°C hasta que esté dorado. Servir con guisantes.',
            'en': '1. Cut potatoes into thick chips. Dry well.\n2. Fry chips twice: first at 130°C, then at 180°C.\n3. Make batter: mix flour, egg, beer and salt.\n4. Coat fish in flour, then in batter.\n5. Fry fish at 180°C until golden. Serve with peas.',
            'fr': '1. Couper les pommes de terre en bâtonnets épais. Bien sécher.\n2. Frire les frites deux fois: d\'abord à 130°C, puis à 180°C.\n3. Faire la pâte: mélanger farine, œuf, bière et sel.\n4. Enrober le poisson de farine, puis de pâte.\n5. Frire le poisson à 180°C jusqu\'à ce qu\'il soit doré. Servir avec des petits pois.',
            'de': '1. Kartoffeln in dicke Stifte schneiden. Gut trocknen.\n2. Pommes zweimal frittieren: erst bei 130°C, dann bei 180°C.\n3. Teig machen: Mehl, Ei, Bier und Salz mischen.\n4. Fisch in Mehl wenden, dann in Teig.\n5. Fisch bei 180°C goldbraun frittieren. Mit Erbsen servieren.'
        },
        'tips': {
            'es': 'La cerveza fría hace que la masa quede más crujiente.',
            'en': 'Cold beer makes the batter crispier.',
            'fr': 'La bière froide rend la pâte plus croustillante.',
            'de': 'Kaltes Bier macht den Teig knuspriger.'
        },
        'tags': ['british', 'fish', 'comfort', 'kids', 'friday']
    },
    
    # =============== RECETAS FRANCESAS ===============
    {
        'id': 'fr001',
        'name': {'es': 'Quiche Lorraine', 'en': 'Quiche Lorraine', 'fr': 'Quiche Lorraine', 'de': 'Quiche Lorraine'},
        'category': 'eggs',
        'image': '🥧',
        'time': 55,
        'difficulty': 'medium',
        'servings': 6,
        'calories': 380,
        'proteins': 14,
        'carbs': 22,
        'fats': 26,
        'fiber': 1,
        'cost': 8.00,
        'ingredients': {
            'es': ['1 masa quebrada', '200g bacon o lardones', '200ml nata', '3 huevos', '100g queso gruyère rallado', 'Nuez moscada', 'Sal y pimienta'],
            'en': ['1 shortcrust pastry', '200g bacon or lardons', '200ml cream', '3 eggs', '100g grated gruyère', 'Nutmeg', 'Salt and pepper'],
            'fr': ['1 pâte brisée', '200g lardons', '200ml crème fraîche', '3 œufs', '100g gruyère râpé', 'Muscade', 'Sel et poivre'],
            'de': ['1 Mürbeteig', '200g Speck oder Lardons', '200ml Sahne', '3 Eier', '100g geriebener Gruyère', 'Muskatnuss', 'Salz und Pfeffer']
        },
        'instructions': {
            'es': '1. Extender la masa en un molde. Pinchar con tenedor. Hornear 10 min a 180°C.\n2. Dorar los lardones sin aceite.\n3. Batir huevos con nata, nuez moscada, sal y pimienta.\n4. Repartir lardones y queso sobre la masa.\n5. Verter la mezcla de huevo. Hornear 35 min a 180°C.',
            'en': '1. Roll out pastry in a tin. Prick with fork. Bake 10 min at 180°C.\n2. Brown the lardons without oil.\n3. Beat eggs with cream, nutmeg, salt and pepper.\n4. Spread lardons and cheese over pastry.\n5. Pour egg mixture. Bake 35 min at 180°C.',
            'fr': '1. Étaler la pâte dans un moule. Piquer à la fourchette. Cuire 10 min à 180°C.\n2. Faire dorer les lardons sans huile.\n3. Battre les œufs avec la crème, la muscade, sel et poivre.\n4. Répartir les lardons et le fromage sur la pâte.\n5. Verser le mélange d\'œufs. Cuire 35 min à 180°C.',
            'de': '1. Teig in einer Form ausrollen. Mit Gabel einstechen. 10 Min bei 180°C backen.\n2. Lardons ohne Öl anbraten.\n3. Eier mit Sahne, Muskat, Salz und Pfeffer verquirlen.\n4. Lardons und Käse auf dem Teig verteilen.\n5. Eiermischung darüber gießen. 35 Min bei 180°C backen.'
        },
        'tips': {
            'es': 'Dejar reposar 5 minutos antes de servir para que cuaje bien.',
            'en': 'Let rest 5 minutes before serving so it sets properly.',
            'fr': 'Laisser reposer 5 minutes avant de servir pour qu\'elle se tienne bien.',
            'de': '5 Minuten ruhen lassen vor dem Servieren, damit sie fest wird.'
        },
        'tags': ['french', 'eggs', 'meat', 'brunch', 'classic']
    },
    {
        'id': 'fr002',
        'name': {'es': 'Ratatouille', 'en': 'Ratatouille', 'fr': 'Ratatouille', 'de': 'Ratatouille'},
        'category': 'vegetarian',
        'image': '🥬',
        'time': 50,
        'difficulty': 'easy',
        'servings': 6,
        'calories': 180,
        'proteins': 4,
        'carbs': 18,
        'fats': 10,
        'fiber': 6,
        'cost': 6.00,
        'ingredients': {
            'es': ['2 berenjenas', '2 calabacines', '2 pimientos (rojo y amarillo)', '4 tomates', '1 cebolla', '3 dientes de ajo', 'Hierbas provenzales', 'Aceite de oliva', 'Sal'],
            'en': ['2 eggplants', '2 zucchini', '2 peppers (red and yellow)', '4 tomatoes', '1 onion', '3 garlic cloves', 'Herbes de Provence', 'Olive oil', 'Salt'],
            'fr': ['2 aubergines', '2 courgettes', '2 poivrons (rouge et jaune)', '4 tomates', '1 oignon', '3 gousses d\'ail', 'Herbes de Provence', 'Huile d\'olive', 'Sel'],
            'de': ['2 Auberginen', '2 Zucchini', '2 Paprika (rot und gelb)', '4 Tomaten', '1 Zwiebel', '3 Knoblauchzehen', 'Kräuter der Provence', 'Olivenöl', 'Salz']
        },
        'instructions': {
            'es': '1. Cortar todas las verduras en dados medianos.\n2. Sofreír la cebolla y el ajo en aceite.\n3. Añadir los pimientos y cocinar 5 min.\n4. Incorporar berenjenas y calabacines. Cocinar 10 min.\n5. Añadir tomates y hierbas. Tapar y cocinar 25 min a fuego lento.',
            'en': '1. Cut all vegetables into medium cubes.\n2. Sauté onion and garlic in oil.\n3. Add peppers and cook 5 min.\n4. Add eggplants and zucchini. Cook 10 min.\n5. Add tomatoes and herbs. Cover and cook 25 min over low heat.',
            'fr': '1. Couper tous les légumes en dés moyens.\n2. Faire revenir l\'oignon et l\'ail dans l\'huile.\n3. Ajouter les poivrons et cuire 5 min.\n4. Incorporer aubergines et courgettes. Cuire 10 min.\n5. Ajouter tomates et herbes. Couvrir et cuire 25 min à feu doux.',
            'de': '1. Alle Gemüse in mittelgroße Würfel schneiden.\n2. Zwiebel und Knoblauch in Öl anbraten.\n3. Paprika hinzufügen und 5 Min kochen.\n4. Auberginen und Zucchini hinzufügen. 10 Min kochen.\n5. Tomaten und Kräuter hinzufügen. Zudecken und 25 Min bei niedriger Hitze kochen.'
        },
        'tips': {
            'es': 'Perfecto como guarnición o con un huevo frito encima.',
            'en': 'Perfect as a side dish or with a fried egg on top.',
            'fr': 'Parfait en accompagnement ou avec un œuf au plat dessus.',
            'de': 'Perfekt als Beilage oder mit einem Spiegelei oben drauf.'
        },
        'tags': ['french', 'vegetarian', 'healthy', 'summer', 'vegan']
    },
    
    # =============== RECETAS ALEMANAS ===============
    {
        'id': 'de001',
        'name': {'es': 'Schnitzel con Patatas', 'en': 'Schnitzel with Potatoes', 'fr': 'Schnitzel aux Pommes de Terre', 'de': 'Schnitzel mit Kartoffeln'},
        'category': 'meat',
        'image': '🥩',
        'time': 35,
        'difficulty': 'easy',
        'servings': 4,
        'calories': 580,
        'proteins': 35,
        'carbs': 45,
        'fats': 28,
        'fiber': 3,
        'cost': 14.00,
        'ingredients': {
            'es': ['4 filetes de cerdo finos (600g)', '100g harina', '2 huevos batidos', '150g pan rallado', '1kg patatas', 'Limón', 'Mantequilla', 'Sal y pimienta'],
            'en': ['4 thin pork cutlets (600g)', '100g flour', '2 beaten eggs', '150g breadcrumbs', '1kg potatoes', 'Lemon', 'Butter', 'Salt and pepper'],
            'fr': ['4 fines escalopes de porc (600g)', '100g farine', '2 œufs battus', '150g chapelure', '1kg pommes de terre', 'Citron', 'Beurre', 'Sel et poivre'],
            'de': ['4 dünne Schweineschnitzel (600g)', '100g Mehl', '2 verquirlte Eier', '150g Semmelbrösel', '1kg Kartoffeln', 'Zitrone', 'Butter', 'Salz und Pfeffer']
        },
        'instructions': {
            'es': '1. Aplanar los filetes con un mazo. Salpimentar.\n2. Pasar por harina, luego huevo, luego pan rallado.\n3. Freír en mantequilla abundante hasta que estén dorados.\n4. Cocer las patatas y hacer puré o servirlas cocidas.\n5. Servir el schnitzel con rodaja de limón.',
            'en': '1. Flatten cutlets with a mallet. Season with salt and pepper.\n2. Coat in flour, then egg, then breadcrumbs.\n3. Fry in plenty of butter until golden.\n4. Boil potatoes and mash or serve boiled.\n5. Serve schnitzel with a lemon wedge.',
            'fr': '1. Aplatir les escalopes avec un maillet. Saler et poivrer.\n2. Passer dans la farine, puis l\'œuf, puis la chapelure.\n3. Frire dans beaucoup de beurre jusqu\'à ce qu\'ils soient dorés.\n4. Cuire les pommes de terre et faire une purée ou servir bouillies.\n5. Servir le schnitzel avec une rondelle de citron.',
            'de': '1. Schnitzel mit einem Fleischklopfer platt klopfen. Mit Salz und Pfeffer würzen.\n2. In Mehl wenden, dann in Ei, dann in Semmelbrösel.\n3. In reichlich Butter goldbraun braten.\n4. Kartoffeln kochen und pürieren oder gekocht servieren.\n5. Schnitzel mit Zitronenscheibe servieren.'
        },
        'tips': {
            'es': 'La carne debe estar muy fina para que quede crujiente.',
            'en': 'The meat should be very thin so it gets crispy.',
            'fr': 'La viande doit être très fine pour être croustillante.',
            'de': 'Das Fleisch sollte sehr dünn sein, damit es knusprig wird.'
        },
        'tags': ['german', 'meat', 'comfort', 'kids', 'classic']
    },
    {
        'id': 'de002',
        'name': {'es': 'Salchichas con Chucrut', 'en': 'Sausages with Sauerkraut', 'fr': 'Saucisses à la Choucroute', 'de': 'Bratwurst mit Sauerkraut'},
        'category': 'meat',
        'image': '🌭',
        'time': 30,
        'difficulty': 'easy',
        'servings': 4,
        'calories': 520,
        'proteins': 22,
        'carbs': 28,
        'fats': 35,
        'fiber': 5,
        'cost': 8.00,
        'ingredients': {
            'es': ['8 salchichas bratwurst', '500g chucrut', '1 cebolla', '1 manzana', '200ml cerveza', '1 cda semillas de alcaravea', 'Mostaza', 'Aceite'],
            'en': ['8 bratwurst sausages', '500g sauerkraut', '1 onion', '1 apple', '200ml beer', '1 tbsp caraway seeds', 'Mustard', 'Oil'],
            'fr': ['8 saucisses bratwurst', '500g choucroute', '1 oignon', '1 pomme', '200ml bière', '1 c.s. graines de carvi', 'Moutarde', 'Huile'],
            'de': ['8 Bratwürste', '500g Sauerkraut', '1 Zwiebel', '1 Apfel', '200ml Bier', '1 EL Kümmel', 'Senf', 'Öl']
        },
        'instructions': {
            'es': '1. Dorar las salchichas en una sartén con poco aceite.\n2. En otra sartén, sofreír la cebolla cortada en juliana.\n3. Añadir la manzana cortada en dados y el chucrut.\n4. Verter la cerveza y las semillas de alcaravea. Cocer 15 min.\n5. Servir las salchichas sobre el chucrut con mostaza.',
            'en': '1. Brown sausages in a pan with little oil.\n2. In another pan, sauté sliced onion.\n3. Add diced apple and sauerkraut.\n4. Pour beer and caraway seeds. Cook 15 min.\n5. Serve sausages over sauerkraut with mustard.',
            'fr': '1. Dorer les saucisses dans une poêle avec peu d\'huile.\n2. Dans une autre poêle, faire revenir l\'oignon émincé.\n3. Ajouter la pomme en dés et la choucroute.\n4. Verser la bière et les graines de carvi. Cuire 15 min.\n5. Servir les saucisses sur la choucroute avec de la moutarde.',
            'de': '1. Bratwürste in einer Pfanne mit wenig Öl anbraten.\n2. In einer anderen Pfanne geschnittene Zwiebel anbraten.\n3. Gewürfelten Apfel und Sauerkraut hinzufügen.\n4. Bier und Kümmel hinzufügen. 15 Min kochen.\n5. Bratwürste auf Sauerkraut mit Senf servieren.'
        },
        'tips': {
            'es': 'La manzana le da un toque dulce que equilibra la acidez del chucrut.',
            'en': 'The apple adds a sweet touch that balances the sauerkraut\'s acidity.',
            'fr': 'La pomme apporte une touche sucrée qui équilibre l\'acidité de la choucroute.',
            'de': 'Der Apfel gibt eine süße Note, die die Säure des Sauerkrauts ausgleicht.'
        },
        'tags': ['german', 'meat', 'comfort', 'winter', 'quick']
    },
    
    # =============== MÁS RECETAS RÁPIDAS ===============
    {
        'id': 'quick001',
        'name': {'es': 'Ensalada César', 'en': 'Caesar Salad', 'fr': 'Salade César', 'de': 'Caesar Salat'},
        'category': 'salad',
        'image': '🥗',
        'time': 15,
        'difficulty': 'easy',
        'servings': 4,
        'calories': 320,
        'proteins': 18,
        'carbs': 12,
        'fats': 24,
        'fiber': 3,
        'cost': 7.00,
        'ingredients': {
            'es': ['1 lechuga romana', '200g pechuga de pollo', '50g parmesano', 'Picatostes', 'Salsa César: mayonesa, anchoas, ajo, limón, mostaza'],
            'en': ['1 romaine lettuce', '200g chicken breast', '50g parmesan', 'Croutons', 'Caesar dressing: mayonnaise, anchovies, garlic, lemon, mustard'],
            'fr': ['1 laitue romaine', '200g blanc de poulet', '50g parmesan', 'Croûtons', 'Sauce César: mayonnaise, anchois, ail, citron, moutarde'],
            'de': ['1 Römersalat', '200g Hähnchenbrust', '50g Parmesan', 'Croutons', 'Caesar-Dressing: Mayonnaise, Sardellen, Knoblauch, Zitrone, Senf']
        },
        'instructions': {
            'es': '1. Cortar la lechuga y ponerla en un bol grande.\n2. Grillar la pechuga y cortarla en tiras.\n3. Preparar la salsa mezclando todos los ingredientes.\n4. Añadir el pollo, parmesano y picatostes a la lechuga.\n5. Aliñar con la salsa César y mezclar bien.',
            'en': '1. Cut lettuce and place in a large bowl.\n2. Grill chicken breast and slice into strips.\n3. Make dressing by mixing all ingredients.\n4. Add chicken, parmesan and croutons to lettuce.\n5. Dress with Caesar sauce and toss well.',
            'fr': '1. Couper la laitue et la mettre dans un grand bol.\n2. Griller le blanc de poulet et le couper en lanières.\n3. Préparer la sauce en mélangeant tous les ingrédients.\n4. Ajouter le poulet, le parmesan et les croûtons à la laitue.\n5. Assaisonner avec la sauce César et bien mélanger.',
            'de': '1. Salat schneiden und in eine große Schüssel geben.\n2. Hähnchenbrust grillen und in Streifen schneiden.\n3. Dressing zubereiten, indem alle Zutaten gemischt werden.\n4. Hähnchen, Parmesan und Croutons zum Salat geben.\n5. Mit Caesar-Sauce anmachen und gut mischen.'
        },
        'tips': {
            'es': 'Las anchoas en la salsa son opcionales pero le dan el sabor auténtico.',
            'en': 'Anchovies in the dressing are optional but give authentic flavor.',
            'fr': 'Les anchois dans la sauce sont optionnels mais donnent le goût authentique.',
            'de': 'Sardellen im Dressing sind optional, geben aber authentischen Geschmack.'
        },
        'tags': ['international', 'salad', 'quick', 'healthy', 'lunch']
    },
    {
        'id': 'quick002',
        'name': {'es': 'Huevos Revueltos con Jamón', 'en': 'Scrambled Eggs with Ham', 'fr': 'Œufs Brouillés au Jambon', 'de': 'Rührei mit Schinken'},
        'category': 'eggs',
        'image': '🥚',
        'time': 10,
        'difficulty': 'easy',
        'servings': 2,
        'calories': 280,
        'proteins': 20,
        'carbs': 2,
        'fats': 22,
        'fiber': 0,
        'cost': 3.00,
        'ingredients': {
            'es': ['4 huevos', '100g jamón serrano', '20g mantequilla', 'Cebollino fresco', 'Sal y pimienta'],
            'en': ['4 eggs', '100g serrano ham', '20g butter', 'Fresh chives', 'Salt and pepper'],
            'fr': ['4 œufs', '100g jambon cru', '20g beurre', 'Ciboulette fraîche', 'Sel et poivre'],
            'de': ['4 Eier', '100g Serrano-Schinken', '20g Butter', 'Frischer Schnittlauch', 'Salz und Pfeffer']
        },
        'instructions': {
            'es': '1. Batir los huevos con sal y pimienta.\n2. Cortar el jamón en trocitos.\n3. Derretir la mantequilla a fuego medio-bajo.\n4. Añadir los huevos y remover constantemente.\n5. Cuando estén cremosos, añadir jamón y cebollino. Servir inmediatamente.',
            'en': '1. Beat eggs with salt and pepper.\n2. Cut ham into small pieces.\n3. Melt butter over medium-low heat.\n4. Add eggs and stir constantly.\n5. When creamy, add ham and chives. Serve immediately.',
            'fr': '1. Battre les œufs avec sel et poivre.\n2. Couper le jambon en petits morceaux.\n3. Faire fondre le beurre à feu moyen-doux.\n4. Ajouter les œufs et remuer constamment.\n5. Quand ils sont crémeux, ajouter jambon et ciboulette. Servir immédiatement.',
            'de': '1. Eier mit Salz und Pfeffer verquirlen.\n2. Schinken in kleine Stücke schneiden.\n3. Butter bei mittlerer Hitze schmelzen.\n4. Eier hinzufügen und ständig rühren.\n5. Wenn cremig, Schinken und Schnittlauch hinzufügen. Sofort servieren.'
        },
        'tips': {
            'es': 'Retirar del fuego antes de que estén del todo hechos, seguirán cuajando.',
            'en': 'Remove from heat before fully set, they will continue cooking.',
            'fr': 'Retirer du feu avant qu\'ils soient complètement cuits, ils continueront à cuire.',
            'de': 'Vom Herd nehmen bevor sie ganz fest sind, sie garen weiter.'
        },
        'tags': ['quick', 'eggs', 'breakfast', 'kids', 'budget']
    },
    
    # =============== RECETAS PARA NIÑOS ===============
    {
        'id': 'kids001',
        'name': {'es': 'Macarrones con Queso', 'en': 'Mac and Cheese', 'fr': 'Macaroni au Fromage', 'de': 'Käse-Makkaroni'},
        'category': 'pasta',
        'image': '🧀',
        'time': 25,
        'difficulty': 'easy',
        'servings': 4,
        'calories': 450,
        'proteins': 18,
        'carbs': 52,
        'fats': 20,
        'fiber': 2,
        'cost': 5.00,
        'ingredients': {
            'es': ['400g macarrones', '200g queso cheddar', '50g mantequilla', '40g harina', '500ml leche', 'Nuez moscada', 'Sal'],
            'en': ['400g macaroni', '200g cheddar cheese', '50g butter', '40g flour', '500ml milk', 'Nutmeg', 'Salt'],
            'fr': ['400g macaroni', '200g cheddar', '50g beurre', '40g farine', '500ml lait', 'Muscade', 'Sel'],
            'de': ['400g Makkaroni', '200g Cheddar-Käse', '50g Butter', '40g Mehl', '500ml Milch', 'Muskatnuss', 'Salz']
        },
        'instructions': {
            'es': '1. Cocer la pasta al dente. Escurrir.\n2. Derretir mantequilla, añadir harina y cocinar 1 min.\n3. Verter la leche poco a poco removiendo.\n4. Añadir el queso rallado y mezclar hasta que se funda.\n5. Combinar con la pasta. Gratinar en horno opcional.',
            'en': '1. Cook pasta al dente. Drain.\n2. Melt butter, add flour and cook 1 min.\n3. Pour milk gradually while stirring.\n4. Add grated cheese and stir until melted.\n5. Combine with pasta. Broil in oven optional.',
            'fr': '1. Cuire les pâtes al dente. Égoutter.\n2. Faire fondre le beurre, ajouter la farine et cuire 1 min.\n3. Verser le lait petit à petit en remuant.\n4. Ajouter le fromage râpé et mélanger jusqu\'à ce qu\'il fonde.\n5. Combiner avec les pâtes. Gratiner au four optionnel.',
            'de': '1. Pasta al dente kochen. Abtropfen.\n2. Butter schmelzen, Mehl hinzufügen und 1 Min kochen.\n3. Milch nach und nach unter Rühren hinzufügen.\n4. Geriebenen Käse hinzufügen und rühren bis er schmilzt.\n5. Mit Pasta mischen. Optional im Ofen überbacken.'
        },
        'tips': {
            'es': 'Añade un poco de mostaza a la salsa para más sabor.',
            'en': 'Add a little mustard to the sauce for more flavor.',
            'fr': 'Ajoutez un peu de moutarde à la sauce pour plus de saveur.',
            'de': 'Etwas Senf zur Sauce geben für mehr Geschmack.'
        },
        'tags': ['international', 'pasta', 'kids', 'comfort', 'quick', 'vegetarian']
    },
    {
        'id': 'kids002',
        'name': {'es': 'Nuggets de Pollo Caseros', 'en': 'Homemade Chicken Nuggets', 'fr': 'Nuggets de Poulet Maison', 'de': 'Hausgemachte Chicken Nuggets'},
        'category': 'meat',
        'image': '🍗',
        'time': 30,
        'difficulty': 'easy',
        'servings': 4,
        'calories': 380,
        'proteins': 28,
        'carbs': 22,
        'fats': 20,
        'fiber': 1,
        'cost': 6.00,
        'ingredients': {
            'es': ['500g pechuga de pollo', '100g pan rallado', '50g harina', '2 huevos', '1 cdta pimentón dulce', 'Aceite para freír', 'Sal'],
            'en': ['500g chicken breast', '100g breadcrumbs', '50g flour', '2 eggs', '1 tsp sweet paprika', 'Oil for frying', 'Salt'],
            'fr': ['500g blanc de poulet', '100g chapelure', '50g farine', '2 œufs', '1 c.c. paprika doux', 'Huile pour friture', 'Sel'],
            'de': ['500g Hähnchenbrust', '100g Semmelbrösel', '50g Mehl', '2 Eier', '1 TL süßer Paprika', 'Öl zum Frittieren', 'Salz']
        },
        'instructions': {
            'es': '1. Cortar el pollo en trozos pequeños. Salpimentar.\n2. Mezclar el pan rallado con el pimentón.\n3. Pasar cada trozo por harina, huevo y pan rallado.\n4. Freír en aceite caliente hasta que estén dorados.\n5. Escurrir sobre papel absorbente.',
            'en': '1. Cut chicken into small pieces. Season with salt and pepper.\n2. Mix breadcrumbs with paprika.\n3. Coat each piece in flour, egg and breadcrumbs.\n4. Fry in hot oil until golden.\n5. Drain on paper towels.',
            'fr': '1. Couper le poulet en petits morceaux. Saler et poivrer.\n2. Mélanger la chapelure avec le paprika.\n3. Enrober chaque morceau de farine, œuf et chapelure.\n4. Frire dans l\'huile chaude jusqu\'à ce qu\'ils soient dorés.\n5. Égoutter sur du papier absorbant.',
            'de': '1. Hähnchen in kleine Stücke schneiden. Mit Salz und Pfeffer würzen.\n2. Semmelbrösel mit Paprika mischen.\n3. Jedes Stück in Mehl, Ei und Semmelbröseln wenden.\n4. In heißem Öl goldbraun frittieren.\n5. Auf Küchenpapier abtropfen lassen.'
        },
        'tips': {
            'es': 'También se pueden hacer al horno a 200°C durante 20 minutos.',
            'en': 'They can also be baked at 200°C for 20 minutes.',
            'fr': 'Ils peuvent aussi être cuits au four à 200°C pendant 20 minutes.',
            'de': 'Sie können auch bei 200°C für 20 Minuten gebacken werden.'
        },
        'tags': ['international', 'meat', 'kids', 'quick', 'comfort']
    },
    {
        'id': 'kids003',
        'name': {'es': 'Pizza Casera', 'en': 'Homemade Pizza', 'fr': 'Pizza Maison', 'de': 'Hausgemachte Pizza'},
        'category': 'quick',
        'image': '🍕',
        'time': 35,
        'difficulty': 'easy',
        'servings': 4,
        'calories': 420,
        'proteins': 16,
        'carbs': 48,
        'fats': 18,
        'fiber': 2,
        'cost': 5.50,
        'ingredients': {
            'es': ['Masa de pizza (o 300g harina, levadura, agua)', '200g tomate triturado', '200g mozzarella', 'Orégano', 'Aceite de oliva', 'Toppings al gusto'],
            'en': ['Pizza dough (or 300g flour, yeast, water)', '200g crushed tomatoes', '200g mozzarella', 'Oregano', 'Olive oil', 'Toppings of choice'],
            'fr': ['Pâte à pizza (ou 300g farine, levure, eau)', '200g tomates concassées', '200g mozzarella', 'Origan', 'Huile d\'olive', 'Garnitures au choix'],
            'de': ['Pizzateig (oder 300g Mehl, Hefe, Wasser)', '200g passierte Tomaten', '200g Mozzarella', 'Oregano', 'Olivenöl', 'Belag nach Wahl']
        },
        'instructions': {
            'es': '1. Estirar la masa sobre papel de horno.\n2. Extender el tomate dejando un borde.\n3. Añadir la mozzarella cortada o rallada.\n4. Añadir los toppings preferidos.\n5. Hornear a 220°C durante 15-18 minutos.',
            'en': '1. Roll out dough on baking paper.\n2. Spread tomato leaving a border.\n3. Add sliced or grated mozzarella.\n4. Add preferred toppings.\n5. Bake at 220°C for 15-18 minutes.',
            'fr': '1. Étaler la pâte sur du papier cuisson.\n2. Étaler la tomate en laissant une bordure.\n3. Ajouter la mozzarella coupée ou râpée.\n4. Ajouter les garnitures préférées.\n5. Cuire à 220°C pendant 15-18 minutes.',
            'de': '1. Teig auf Backpapier ausrollen.\n2. Tomaten verteilen, Rand frei lassen.\n3. Geschnittenen oder geriebenen Mozzarella hinzufügen.\n4. Lieblingsbelag hinzufügen.\n5. Bei 220°C 15-18 Minuten backen.'
        },
        'tips': {
            'es': 'Deja participar a los niños eligiendo y poniendo sus ingredientes.',
            'en': 'Let kids participate by choosing and adding their ingredients.',
            'fr': 'Laissez les enfants participer en choisissant et ajoutant leurs ingrédients.',
            'de': 'Lassen Sie die Kinder beim Auswählen und Belegen mitmachen.'
        },
        'tags': ['international', 'quick', 'kids', 'comfort', 'family', 'vegetarian']
    },
]

# =====================================================
# ESTADO DE LA APLICACIÓN
# =====================================================

if 'language' not in st.session_state:
    st.session_state.language = 'es'

if 'weekly_menu' not in st.session_state:
    st.session_state.weekly_menu = {day: {'lunch': None, 'dinner': None} 
                                     for day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']}

if 'favorites' not in st.session_state:
    st.session_state.favorites = []

if 'shopping_list' not in st.session_state:
    st.session_state.shopping_list = []

if 'family' not in st.session_state:
    st.session_state.family = {
        'adults': 2,
        'children': 2,
        'budget': 100,
        'allergies': [],
        'preferences': []
    }

if 'current_page' not in st.session_state:
    st.session_state.current_page = 'menu'

# =====================================================
# FUNCIONES
# =====================================================

def t(key):
    """Obtiene la traducción"""
    lang = st.session_state.language
    return TRANSLATIONS.get(lang, TRANSLATIONS['es']).get(key, key)

def get_recipe_text(recipe, field):
    """Obtiene el texto de una receta en el idioma actual"""
    lang = st.session_state.language
    if isinstance(recipe.get(field), dict):
        return recipe[field].get(lang, recipe[field].get('en', ''))
    return recipe.get(field, '')

def get_recipes_list():
    """Obtiene la lista de recetas"""
    return RECIPES_DB

def filter_recipes(search='', category='all', max_time=None, difficulty=None):
    """Filtra las recetas"""
    recipes = get_recipes_list()
    lang = st.session_state.language
    
    filtered = []
    for r in recipes:
        name = get_recipe_text(r, 'name').lower()
        
        # Filtro de búsqueda
        if search and search.lower() not in name:
            continue
        
        # Filtro de categoría
        if category != 'all' and r.get('category') != category:
            continue
        
        # Filtro de tiempo
        if max_time and r.get('time', 0) > max_time:
            continue
        
        # Filtro de dificultad
        if difficulty and r.get('difficulty') != difficulty:
            continue
        
        filtered.append(r)
    
    return filtered

def generate_menu():
    """Genera un menú automático"""
    recipes = get_recipes_list()
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    used = set()
    for day in days:
        available = [r for r in recipes if r['id'] not in used]
        if len(available) >= 2:
            lunch = random.choice(available)
            used.add(lunch['id'])
            available = [r for r in available if r['id'] != lunch['id']]
            dinner = random.choice(available)
            used.add(dinner['id'])
            st.session_state.weekly_menu[day] = {'lunch': lunch, 'dinner': dinner}

def clear_menu():
    """Limpia el menú"""
    for day in st.session_state.weekly_menu:
        st.session_state.weekly_menu[day] = {'lunch': None, 'dinner': None}

def generate_shopping_list():
    """Genera lista de compra del menú"""
    items = {}
    lang = st.session_state.language
    
    for day, meals in st.session_state.weekly_menu.items():
        for meal_type, recipe in meals.items():
            if recipe:
                ingredients = recipe.get('ingredients', {}).get(lang, [])
                for ing in ingredients:
                    if ing in items:
                        items[ing] += 1
                    else:
                        items[ing] = 1
    
    st.session_state.shopping_list = [{'item': k, 'qty': v, 'bought': False} for k, v in items.items()]

def get_menu_stats():
    """Obtiene estadísticas del menú"""
    total_cal = 0
    total_cost = 0
    total_time = 0
    count = 0
    
    for day, meals in st.session_state.weekly_menu.items():
        for meal_type, recipe in meals.items():
            if recipe:
                total_cal += recipe.get('calories', 0)
                total_cost += recipe.get('cost', 0)
                total_time += recipe.get('time', 0)
                count += 1
    
    return {
        'meals': count,
        'calories': total_cal,
        'cost': total_cost,
        'time': total_time
    }

# =====================================================
# CSS MEJORADO
# =====================================================

st.markdown("""
<style>
    /* Variables de color */
    :root {
        --primary: #FF6B35;
        --primary-dark: #E55A2B;
        --primary-light: #FFF5F0;
        --secondary: #4ECDC4;
        --dark: #2C3E50;
        --light: #F8F9FA;
        --success: #27AE60;
        --warning: #F39C12;
    }
    
    /* Reset y base */
    .main > div {
        padding-top: 0;
    }
    
    /* Header principal */
    .app-header {
        background: linear-gradient(135deg, #FF6B35 0%, #FF8E53 100%);
        padding: 1.5rem 2rem;
        border-radius: 0 0 20px 20px;
        margin: -1rem -1rem 1.5rem -1rem;
        color: white;
        box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3);
    }
    
    .app-header h1 {
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .app-header p {
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
        font-size: 1rem;
    }
    
    /* Cards de recetas mejoradas */
    .recipe-card {
        background: white;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border: 1px solid #f0f0f0;
    }
    
    .recipe-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 25px rgba(255,107,53,0.15);
    }
    
    .recipe-card-image {
        background: linear-gradient(135deg, #FFF5F0 0%, #FFE8E0 100%);
        padding: 1.5rem;
        text-align: center;
        font-size: 4rem;
    }
    
    .recipe-card-content {
        padding: 1rem;
    }
    
    .recipe-card-title {
        font-weight: 600;
        color: #2C3E50;
        margin-bottom: 0.5rem;
        font-size: 1rem;
    }
    
    .recipe-card-meta {
        display: flex;
        gap: 1rem;
        font-size: 0.8rem;
        color: #888;
    }
    
    .recipe-card-meta span {
        display: flex;
        align-items: center;
        gap: 4px;
    }
    
    /* Calendario semanal mejorado */
    .day-column {
        background: white;
        border-radius: 12px;
        padding: 0.8rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .day-header {
        text-align: center;
        font-weight: 600;
        color: #FF6B35;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #FFF5F0;
        margin-bottom: 0.5rem;
    }
    
    .meal-slot {
        background: #FAFAFA;
        border-radius: 10px;
        padding: 0.6rem;
        margin: 0.4rem 0;
        min-height: 70px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        border: 2px dashed #E0E0E0;
        transition: all 0.2s ease;
    }
    
    .meal-slot:hover {
        border-color: #FF6B35;
        background: #FFF5F0;
    }
    
    .meal-slot.filled {
        background: linear-gradient(135deg, #FFF5F0 0%, #FFE8E0 100%);
        border: 2px solid #FF6B35;
    }
    
    .meal-emoji {
        font-size: 1.8rem;
        margin-bottom: 0.2rem;
    }
    
    .meal-name {
        font-size: 0.75rem;
        color: #555;
        text-align: center;
        line-height: 1.2;
    }
    
    .meal-label {
        font-size: 0.65rem;
        color: #888;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.3rem;
    }
    
    /* Estadísticas */
    .stats-container {
        display: flex;
        gap: 1rem;
        margin: 1rem 0;
    }
    
    .stat-card {
        background: white;
        padding: 1rem;
        border-radius: 12px;
        text-align: center;
        flex: 1;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    
    .stat-value {
        font-size: 1.5rem;
        font-weight: 700;
        color: #FF6B35;
    }
    
    .stat-label {
        font-size: 0.8rem;
        color: #888;
        margin-top: 0.2rem;
    }
    
    /* Lista de compra */
    .shopping-item {
        display: flex;
        align-items: center;
        padding: 0.8rem 1rem;
        background: white;
        border-radius: 10px;
        margin: 0.4rem 0;
        box-shadow: 0 1px 4px rgba(0,0,0,0.05);
    }
    
    .shopping-item.bought {
        opacity: 0.5;
        text-decoration: line-through;
    }
    
    /* Premium banner */
    .premium-banner {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 16px;
        padding: 1.5rem;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    
    .premium-banner h3 {
        margin: 0 0 0.5rem 0;
    }
    
    .premium-features {
        text-align: left;
        margin: 1rem 0;
    }
    
    .premium-price {
        font-size: 2rem;
        font-weight: 700;
        margin: 1rem 0;
    }
    
    /* Botones mejorados */
    .stButton > button {
        background: linear-gradient(135deg, #FF6B35 0%, #FF8E53 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.2rem;
        font-weight: 500;
        transition: all 0.2s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(255,107,53,0.3);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #FFF8F5 0%, #FFFFFF 100%);
    }
    
    [data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
    }
    
    /* Nutrición badges */
    .nutrition-badge {
        display: inline-flex;
        align-items: center;
        gap: 4px;
        background: #F5F5F5;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.8rem;
        color: #555;
    }
    
    .nutrition-badge.calories {
        background: #FFF3E0;
        color: #E65100;
    }
    
    .nutrition-badge.protein {
        background: #E3F2FD;
        color: #1565C0;
    }
    
    .nutrition-badge.time {
        background: #E8F5E9;
        color: #2E7D32;
    }
    
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
</style>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:
    # Logo
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0 2rem 0;">
        <span style="font-size: 3.5rem;">🍽️</span>
        <h1 style="color: #FF6B35; margin: 0.5rem 0 0 0; font-size: 1.8rem;">FamFood</h1>
        <p style="color: #888; font-size: 0.9rem; margin: 0;">Smart Meal Planner</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Selector de idioma
    st.markdown(f"#### 🌍 {t('language')}")
    lang_options = {'es': '🇪🇸 Español', 'en': '🇬🇧 English', 'fr': '🇫🇷 Français', 'de': '🇩🇪 Deutsch'}
    
    selected_lang = st.selectbox(
        "lang",
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
    nav_items = [
        ('menu', t('nav_menu')),
        ('recipes', t('nav_recipes')),
        ('shopping', t('nav_shopping')),
        ('family', t('nav_family')),
        ('ai', t('nav_ai')),
        ('favorites', t('nav_favorites')),
    ]
    
    for key, label in nav_items:
        if st.button(label, key=f"nav_{key}", use_container_width=True):
            st.session_state.current_page = key
            st.rerun()
    
    st.divider()
    
    # Stats rápidos
    stats = get_menu_stats()
    st.markdown(f"""
    <div style="background: #FFF5F0; padding: 1rem; border-radius: 12px;">
        <p style="margin: 0 0 0.5rem 0; font-weight: 600; color: #FF6B35;">📊 Esta semana</p>
        <p style="margin: 0.2rem 0; font-size: 0.85rem;">🍽️ {stats['meals']}/14 comidas</p>
        <p style="margin: 0.2rem 0; font-size: 0.85rem;">💰 ~{stats['cost']:.0f}€ estimado</p>
        <p style="margin: 0.2rem 0; font-size: 0.85rem;">🔥 ~{stats['calories']} kcal total</p>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# CONTENIDO PRINCIPAL
# =====================================================

# Header
st.markdown(f"""
<div class="app-header">
    <h1>🍽️ FamFood</h1>
    <p>{t('tagline')}</p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# PÁGINA: MENÚ SEMANAL
# =====================================================

if st.session_state.current_page == 'menu':
    
    # Botones de acción
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button(t('generate_menu'), use_container_width=True):
            generate_menu()
            st.rerun()
    with col2:
        if st.button(t('clear_menu'), use_container_width=True):
            clear_menu()
            st.rerun()
    with col3:
        if st.button(t('generate_list'), use_container_width=True):
            generate_shopping_list()
            st.success("✅")
    with col4:
        st.button(t('copy_week'), use_container_width=True, disabled=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Calendario semanal
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    short_days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    
    cols = st.columns(7)
    
    for i, (day, short) in enumerate(zip(days, short_days)):
        with cols[i]:
            st.markdown(f"""
            <div class="day-column">
                <div class="day-header">{t(short).upper()}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Comida
            lunch = st.session_state.weekly_menu[day].get('lunch')
            st.markdown(f'<div class="meal-label">🌞 {t("lunch")}</div>', unsafe_allow_html=True)
            
            if lunch:
                st.markdown(f"""
                <div class="meal-slot filled">
                    <div class="meal-emoji">{lunch['image']}</div>
                    <div class="meal-name">{get_recipe_text(lunch, 'name')[:18]}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="meal-slot">
                    <span style="color: #ccc; font-size: 1.5rem;">+</span>
                </div>
                """, unsafe_allow_html=True)
            
            # Cena
            dinner = st.session_state.weekly_menu[day].get('dinner')
            st.markdown(f'<div class="meal-label">🌙 {t("dinner")}</div>', unsafe_allow_html=True)
            
            if dinner:
                st.markdown(f"""
                <div class="meal-slot filled">
                    <div class="meal-emoji">{dinner['image']}</div>
                    <div class="meal-name">{get_recipe_text(dinner, 'name')[:18]}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="meal-slot">
                    <span style="color: #ccc; font-size: 1.5rem;">+</span>
                </div>
                """, unsafe_allow_html=True)
    
    # Estadísticas
    st.markdown("<br>", unsafe_allow_html=True)
    stats = get_menu_stats()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🍽️ Comidas", f"{stats['meals']}/14")
    with col2:
        st.metric("🔥 Calorías", f"{stats['calories']:,} kcal")
    with col3:
        st.metric("💰 Coste", f"{stats['cost']:.2f}€")
    with col4:
        st.metric("⏱️ Tiempo total", f"{stats['time']} min")

# =====================================================
# PÁGINA: RECETAS
# =====================================================

elif st.session_state.current_page == 'recipes':
    
    # Filtros
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        search = st.text_input("🔍", placeholder=t('search_recipes'), label_visibility="collapsed")
    
    with col2:
        categories = ['all', 'meat', 'fish', 'vegetarian', 'pasta', 'rice', 'soup', 'salad', 'eggs', 'legumes']
        category = st.selectbox(
            "cat",
            categories,
            format_func=lambda x: t(f'cat_{x}') if x != 'all' else t('all_categories'),
            label_visibility="collapsed"
        )
    
    with col3:
        difficulty = st.selectbox(
            "diff",
            [None, 'easy', 'medium', 'hard'],
            format_func=lambda x: t('all_categories') if x is None else t(f'diff_{x}'),
            label_visibility="collapsed"
        )
    
    st.divider()
    
    # Obtener recetas filtradas
    recipes = filter_recipes(search, category, difficulty=difficulty)
    
    if not recipes:
        st.info(t('no_results'))
    else:
        # Grid de recetas
        cols = st.columns(3)
        
        for i, recipe in enumerate(recipes):
            with cols[i % 3]:
                with st.container():
                    st.markdown(f"""
                    <div class="recipe-card">
                        <div class="recipe-card-image">{recipe['image']}</div>
                        <div class="recipe-card-content">
                            <div class="recipe-card-title">{get_recipe_text(recipe, 'name')}</div>
                            <div class="recipe-card-meta">
                                <span>⏱️ {recipe['time']} {t('min')}</span>
                                <span>🔥 {recipe['calories']} kcal</span>
                                <span>👥 {recipe['servings']}</span>
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    with st.expander(t('view_recipe')):
                        # Info nutricional
                        st.markdown(f"**{t('nutrition_info')} ({t('per_serving')}):**")
                        col_a, col_b, col_c, col_d = st.columns(4)
                        with col_a:
                            st.markdown(f"🔥 **{recipe['calories']}** kcal")
                        with col_b:
                            st.markdown(f"🥩 **{recipe['proteins']}g** prot")
                        with col_c:
                            st.markdown(f"🍞 **{recipe['carbs']}g** carbs")
                        with col_d:
                            st.markdown(f"🧈 **{recipe['fats']}g** fat")
                        
                        st.markdown(f"**{t('ingredients')}:**")
                        ingredients = get_recipe_text(recipe, 'ingredients')
                        if isinstance(ingredients, list):
                            for ing in ingredients:
                                st.markdown(f"• {ing}")
                        
                        st.markdown(f"**{t('instructions')}:**")
                        st.write(get_recipe_text(recipe, 'instructions'))
                        
                        st.markdown(f"💡 **{t('tips')}:** {get_recipe_text(recipe, 'tips')}")
                        
                        # Botones
                        col_btn1, col_btn2 = st.columns(2)
                        with col_btn1:
                            if st.button(t('add_to_menu'), key=f"add_{recipe['id']}"):
                                # Añadir al primer slot vacío
                                for day in st.session_state.weekly_menu:
                                    if st.session_state.weekly_menu[day]['lunch'] is None:
                                        st.session_state.weekly_menu[day]['lunch'] = recipe
                                        st.success("✅")
                                        break
                                    elif st.session_state.weekly_menu[day]['dinner'] is None:
                                        st.session_state.weekly_menu[day]['dinner'] = recipe
                                        st.success("✅")
                                        break

# =====================================================
# PÁGINA: LISTA DE COMPRA
# =====================================================

elif st.session_state.current_page == 'shopping':
    
    st.subheader(f"🛒 {t('shopping_list')}")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button(t('generate_list'), use_container_width=True):
            generate_shopping_list()
            st.rerun()
    with col2:
        if st.button(t('clear_list'), use_container_width=True):
            st.session_state.shopping_list = []
            st.rerun()
    with col3:
        if st.session_state.shopping_list:
            # Generar texto para WhatsApp
            items_text = "\n".join([f"{'✅' if item['bought'] else '⬜'} {item['item']}" 
                                    for item in st.session_state.shopping_list])
            wa_text = f"🛒 *{t('shopping_list')} - FamFood*\n\n{items_text}"
            st.markdown(f"[{t('share_whatsapp')}](https://wa.me/?text={wa_text})")
    
    st.divider()
    
    if not st.session_state.shopping_list:
        st.info(f"📝 {t('no_results')}. {t('generate_list')}.")
    else:
        # Mostrar items
        for i, item in enumerate(st.session_state.shopping_list):
            col1, col2 = st.columns([4, 1])
            with col1:
                bought = st.checkbox(
                    item['item'],
                    value=item['bought'],
                    key=f"shop_{i}"
                )
                st.session_state.shopping_list[i]['bought'] = bought
            with col2:
                st.write(f"x{item['qty']}")
        
        # Progreso
        st.divider()
        total = len(st.session_state.shopping_list)
        bought = sum(1 for item in st.session_state.shopping_list if item['bought'])
        st.progress(bought / total if total > 0 else 0)
        st.write(f"✅ {bought}/{total} {t('items_bought')}")

# =====================================================
# PÁGINA: FAMILIA
# =====================================================

elif st.session_state.current_page == 'family':
    
    st.subheader(f"👨‍👩‍👧‍👦 {t('family_profile')}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"**{t('num_people')}**")
        adults = st.number_input(t('adults'), 1, 10, st.session_state.family['adults'])
        children = st.number_input(t('children'), 0, 10, st.session_state.family['children'])
        
        st.markdown(f"**{t('weekly_budget')}**")
        budget = st.slider("€", 30, 300, st.session_state.family['budget'])
        
        st.session_state.family['adults'] = adults
        st.session_state.family['children'] = children
        st.session_state.family['budget'] = budget
    
    with col2:
        st.markdown(f"**{t('allergies')}**")
        allergies = ['gluten', 'lactose', 'nuts', 'eggs', 'fish', 'shellfish', 'soy']
        selected_allergies = []
        for allergy in allergies:
            if st.checkbox(t(f'allergy_{allergy}'), key=f"allergy_{allergy}"):
                selected_allergies.append(allergy)
        st.session_state.family['allergies'] = selected_allergies
        
        st.markdown(f"**{t('preferences')}**")
        prefs = ['no_pork', 'vegetarian', 'quick_meals', 'budget_friendly']
        selected_prefs = []
        for pref in prefs:
            if st.checkbox(t(f'pref_{pref}'), key=f"pref_{pref}"):
                selected_prefs.append(pref)
        st.session_state.family['preferences'] = selected_prefs
    
    st.divider()
    
    # Premium banner
    st.markdown(f"""
    <div class="premium-banner">
        <h3>{t('premium_title')}</h3>
        <p>{t('premium_subtitle')}</p>
        <div class="premium-features">
            <p>{t('premium_feature_1')}</p>
            <p>{t('premium_feature_2')}</p>
            <p>{t('premium_feature_3')}</p>
            <p>{t('premium_feature_4')}</p>
            <p>{t('premium_feature_5')}</p>
        </div>
        <div class="premium-price">{t('premium_price')}</div>
        <button style="background: white; color: #667eea; border: none; padding: 0.8rem 2rem; border-radius: 25px; font-weight: 600; cursor: pointer;">
            {t('premium_trial')}
        </button>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# PÁGINA: ASISTENTE IA
# =====================================================

elif st.session_state.current_page == 'ai':
    
    st.subheader(f"🤖 {t('ai_assistant')}")
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 100%); padding: 1.5rem; border-radius: 16px; margin-bottom: 1rem;">
        <p style="margin: 0; font-size: 1.1rem;">
            💡 Dime qué ingredientes tienes y te sugiero recetas perfectas para tu familia.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Input de ingredientes
    ingredients_input = st.text_area(
        t('ai_whats_in_fridge'),
        placeholder=t('ai_placeholder'),
        height=100
    )
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button(t('ai_search'), use_container_width=True):
            if ingredients_input:
                # Buscar recetas que contengan los ingredientes
                keywords = ingredients_input.lower().split()
                matching = []
                
                for recipe in RECIPES_DB:
                    ingredients = get_recipe_text(recipe, 'ingredients')
                    if isinstance(ingredients, list):
                        ing_text = ' '.join(ingredients).lower()
                        if any(kw in ing_text for kw in keywords):
                            matching.append(recipe)
                
                if matching:
                    st.success(f"✅ {len(matching)} {t('ai_results')}")
                    for recipe in matching[:5]:
                        st.markdown(f"**{recipe['image']} {get_recipe_text(recipe, 'name')}** - {recipe['time']} min")
                else:
                    st.warning(t('no_results'))
    
    with col2:
        if st.button(t('ai_suggest_menu'), use_container_width=True):
            generate_menu()
            st.success("✅ Menu generado!")
    
    st.divider()
    
    # Botones de sugerencias rápidas
    st.markdown("**Sugerencias rápidas:**")
    quick_cols = st.columns(4)
    
    quick_suggestions = [
        (t('ai_healthier_option'), '💚'),
        (t('ai_cheaper_option'), '💰'),
        (t('ai_faster_option'), '⚡'),
        (t('cat_kids'), '👶')
    ]
    
    for i, (label, emoji) in enumerate(quick_suggestions):
        with quick_cols[i]:
            st.button(f"{emoji} {label}", use_container_width=True, disabled=True)

# =====================================================
# PÁGINA: FAVORITOS
# =====================================================

elif st.session_state.current_page == 'favorites':
    
    st.subheader(f"⭐ {t('nav_favorites')}")
    
    if not st.session_state.favorites:
        st.info("No tienes recetas favoritas todavía. Explora las recetas y añade tus favoritas.")
    else:
        cols = st.columns(3)
        for i, recipe_id in enumerate(st.session_state.favorites):
            recipe = next((r for r in RECIPES_DB if r['id'] == recipe_id), None)
            if recipe:
                with cols[i % 3]:
                    st.markdown(f"""
                    <div class="recipe-card">
                        <div class="recipe-card-image">{recipe['image']}</div>
                        <div class="recipe-card-content">
                            <div class="recipe-card-title">{get_recipe_text(recipe, 'name')}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #888; padding: 2rem; border-top: 1px solid #eee;">
    <p>🍽️ <strong>FamFood</strong> v2.0 PRO</p>
    <p style="font-size: 0.8rem;">Planifica • Cocina • Disfruta en familia</p>
    <p style="font-size: 0.75rem; color: #aaa;">© 2024 FamFood - Smart Meal Planning</p>
</div>
""", unsafe_allow_html=True)
