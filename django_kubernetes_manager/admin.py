# -*- coding: utf-8 -*-
from django.contrib import admin
from reversion.admin import VersionAdmin
from solo.admin import SingletonModelAdmin

from .models import AppConfig, JobDefinition, JobInstance, LogEntry, TargetCluster, TelemetryEntry

admin.site.register(AppConfig, SingletonModelAdmin)


@admin.register(JobDefinition)
class JobDefinitionAdmin(VersionAdmin):
    list_display = (
        "id",
        "title",
        "slug",
        "description",
        "lineage_id",
        "parent",
        "image_name",
        "image_tag",
        "command",
        "script",
        "cluster",
        "config",
    )
    list_filter = (
        "parent",
        "cluster",
    )
    search_fields = ("slug",)


@admin.register(LogEntry)
class LogEntryAdmin(VersionAdmin):
    list_display = (
        "id",
        "lineage_id",
        "as_of",
        "message",
        "job_instance",
        "pod_id",
        "source",
    )
    list_filter = (
        "as_of",
        "job_instance",
    )


@admin.register(TelemetryEntry)
class TelemetryEntryAdmin(VersionAdmin):
    list_display = (
        "id",
        "lineage_id",
        "as_of",
        "data_hash",
        "data",
        "job_instance",
    )
    list_filter = (
        "as_of",
        "job_instance",
    )


@admin.register(JobInstance)
class JobInstanceAdmin(VersionAdmin):
    list_display = (
        "id",
        "notes",
        "job_definition",
        "env_vars",
        "script",
        "namespace",
        "timestamps",
        "cluster",
        "config",
    )
    list_filter = (
        "job_definition",
        "cluster",
    )


@admin.register(TargetCluster)
class TargetClusterAdmin(VersionAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "api_endpoint",
        "telemetry_endpoint",
        "telemetry_source",
        "config",
    )
