"""DNSBL related views."""

from django.views import generic

from django.utils.translation import ugettext as _

from django.contrib.auth import mixins as auth_mixins

from .. import models


class DNSBLDomainDetailView(
        auth_mixins.PermissionRequiredMixin, generic.DetailView):
    """DetailView for Domain."""

    model = models.Domain
    permission_required = "admin.view_domain"
    template_name = "admin/dnsbl_domain_detail.html"

    def get_queryset(self):
        """Add some prefetching."""
        return (
            super(DNSBLDomainDetailView, self).get_queryset()
            .prefetch_related("dnsblresult_set"))

    def get_context_data(self, **kwargs):
        """Add extra variables."""
        context = super(DNSBLDomainDetailView, self).get_context_data(**kwargs)
        context.update({
            "title": _("DNSBL summary for {}").format(self.object.name)
        })
        return context
