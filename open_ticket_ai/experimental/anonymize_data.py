# Installationen und Modelldownload (falls noch nicht geschehen)
"""
# Anonymization Module

This module provides functionality to anonymize sensitive personal information (PII) in German text.

It uses:
- spaCy for named entity recognition (NER) to identify persons, organizations, and locations
- Regular expressions to detect email addresses, phone numbers, IBANs, and addresses
- The Faker library to generate realistic replacement data for German context

The main function `anonymize_text` processes input text and replaces:
- Person names with randomly generated names
- Organization names with fake company names
- Locations with fake city names
- Email addresses with fake email addresses
- Valid German phone numbers with fake phone numbers
- IBANs with fake IBANs
- German-style addresses with fake street addresses

Example usage: