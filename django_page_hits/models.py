from django.db import models
from django.utils.translation import ugettext_lazy as _


class PageHit(models.Model):
    """
    Model to save the hit counts for any urls.
    """
    url = models.CharField(_('URL'), max_length=2000)
    visit_date = models.DateField(_('Visit date'), editable=False)
    modified_at = models.DateTimeField(_('Modified'), auto_now=True,
                                       editable=False)
    anonymous_hits = models.PositiveIntegerField(_('Anonymous user Hits'),
                                                 default=0)
    created_at = models.DateTimeField(_('Created'), auto_now_add=True,
                                      editable=False)
    registered_hits = models.PositiveIntegerField(_('Registered user hits'),
                                                  default=0)

    class Meta:
        ordering = ('-visit_date', '-modified_at')
        get_latest_by = 'created_at'
