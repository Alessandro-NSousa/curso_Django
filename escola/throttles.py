from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class AnonRateThrottleCustom(AnonRateThrottle):
    rate = '5/day'  # Limite de 5 requisições por dia para usuários anônimos