from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_facebook_link(value):
    validator = URLValidator()
    try:
        validator(value)
        if "facebook.com" not in value:
            raise ValidationError("Le lien doit être un lien Facebook.")
    except ValidationError as e:
        raise ValidationError("Format de lien invalide.")


def validate_instagram_link(value):
    validator = URLValidator()
    try:
        validator(value)
        if "instagram.com" not in value:
            raise ValidationError("Le lien doit être un lien Instagram.")
    except ValidationError as e:
        raise ValidationError("Format de lien invalide.")

def validate_x_link(value):
    validator = URLValidator()
    try:
        validator(value)
        if "twitter.com" not in value:
            raise ValidationError("Le lien doit être un lien Twitter.")
    except ValidationError as e:
        raise ValidationError("Format de lien invalide.")

def validate_tiktok_link(value):
    validator = URLValidator()
    try:
        validator(value)
        if "tiktok.com" not in value:
            raise ValidationError("Le lien doit être un lien TikTok.")
    except ValidationError as e:
        raise ValidationError("Format de lien invalide.")
    

def validate_linkedin_link(value):
    validator = URLValidator()
    try:
        validator(value)
        if "linkedin.com" not in value:
            raise ValidationError("Le lien doit être un lien LinkedIn.")
    except ValidationError as e:
        raise ValidationError("Format de lien invalide.")

def validate_youtube_link(value):
    validator = URLValidator()
    try:
        validator(value)
        if "youtube.com" not in value:
            raise ValidationError("Le lien doit être un lien YouTube.")
    except ValidationError as e:
        raise ValidationError("Format de lien invalide.")
    

def validate_medium_link(value):
    validator = URLValidator()
    try:
        validator(value)
        if "medium.com" not in value:
            raise ValidationError("Le lien doit être un lien Medium.")
    except ValidationError as e:
        raise ValidationError("Format de lien invalide.")

def validate_pinterest_link(value):
    validator = URLValidator()
    try:
        validator(value)
        if "pinterest.com" not in value:
            raise ValidationError("Le lien doit être un lien Pinterest.")
    except ValidationError as e:
        raise ValidationError("Format de lien invalide.")
    

def validate_reddit_link(value):
    validator = URLValidator()
    try:
        validator(value)
        if "reddit.com" not in value:
            raise ValidationError("Le lien doit être un lien Reddit.")
    except ValidationError as e:
        raise ValidationError("Format de lien invalide.")

def validate_snapchat_link(value):
    validator = URLValidator()
    try:
        validator(value)
        if "snapchat.com" not in value:
            raise ValidationError("Le lien doit être un lien Snapchat.")
    except ValidationError as e:
        raise ValidationError("Format de lien invalide.")

def validate_whatsapp_business_link(value):
    validator = URLValidator()
    try:
        validator(value)
        if "whatsapp.com" not in value:
            raise ValidationError("Le lien doit être un lien Whatsapp Business.")
    except ValidationError as e:
        raise ValidationError("Format de lien invalide.")


def validate_quora_link(value):
    validator = URLValidator()
    try:
        validator(value)
        if "quora.com" not in value:
            raise ValidationError("Le lien doit être un lien Quora.")
    except ValidationError as e:
        raise ValidationError("Format de lien invalide.")
    



# facebook = models.URLField(blank=True, validators=[validate_facebook_link])
# instagram = models.URLField(blank=True, validators=[validate_instagram_link])
# x = models.URLField(blank=True, validators=[validate_x_link])
# whatsapp_business = models.URLField(blank=True, validators=[validate_whatsapp_business_link])
# quora = models.URLField(blank=True, validators=[validate_quora_link])
# reddit = models.URLField(blank=True, validators=[validate_reddit_link])
# snapchat = models.URLField(blank=True, validators=[validate_snapchat_link])
# pinterest = models.URLField(blank=True, validators=[validate_pinterest_link])
# youtube = models.URLField(blank=True, validators=[validate_youtube_link])
# linkedin = models.URLField(blank=True, validators=[validate_linkedin_link])
# medium = models.URLField(blank=True, validators=[validate_medium_link])
# tiktok = models.URLField(blank=True, validators=[validate_tiktok_link])