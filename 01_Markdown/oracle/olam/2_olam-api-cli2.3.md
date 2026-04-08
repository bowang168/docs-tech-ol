---
title: "Oracle Linux Automation Manager 2.3: CLI and API Reference"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "olam"
  - "automation"
type: "oracle-doc"
sensitivity: public
---

This document describes the Oracle Linux Automation Manager Command Line Interface and REST API.

You can view a list of all [**REST Endpoints**](rest-endpoints.html).

---

[Title and Copyright Information](#copyright-information)

Oracle Linux Automation Manager CLI and API Reference Guide

G37196-01

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr) 2025 Oracle and/or its affiliates.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/rest-endpoints.html -->

Sort by

Task

 Path

 Method

Group by API

API

The operations from the API category.

[Debug List](op-api-debug-get.html)
:   Method: get

    Path: `/api/debug/`

[List](op-api-get.html)
:   Method: get

    Path: `/api/`

[Read](op-api-v2-get.html)
:   Method: get

    Path: `/api/v2/`

[Token Handling Using OAuth2](op-api-o-get.html)
:   Method: get

    Path: `/api/o/`

Activity Stream

REST API endpoints for Activity Stream

[List Activity Streams](op-api-v2-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/activity_stream/`

[Retrieve an Activity Stream](op-api-v2-activity_stream-id-get.html)
:   Method: get

    Path: `/api/v2/activity_stream/{id}/`

Ad Hoc Command Events

REST API endpoints for Ad Hoc Command Events

[Retrieve an Ad Hoc Command Event](op-api-v2-ad_hoc_command_events-id-get.html)
:   Method: get

    Path: `/api/v2/ad_hoc_command_events/{id}/`

Ad Hoc Commands

REST API endpoints for Ad Hoc Commands

[Create an Ad Hoc Command](op-api-v2-ad_hoc_commands-post.html)
:   Method: post

    Path: `/api/v2/ad_hoc_commands/`

[Delete an Ad Hoc Command](op-api-v2-ad_hoc_commands-id-delete.html)
:   Method: delete

    Path: `/api/v2/ad_hoc_commands/{id}/`

[List Activity Streams for an Ad Hoc Command](op-api-v2-ad_hoc_commands-id-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/ad_hoc_commands/{id}/activity_stream/`

[List Ad Hoc Command Events for an Ad Hoc Command](op-api-v2-ad_hoc_commands-id-events-get.html)
:   Method: get

    Path: `/api/v2/ad_hoc_commands/{id}/events/`

[List Ad Hoc Commands](op-api-v2-ad_hoc_commands-get.html)
:   Method: get

    Path: `/api/v2/ad_hoc_commands/`

[List Notifications for an Ad Hoc Command](op-api-v2-ad_hoc_commands-id-notifications-get.html)
:   Method: get

    Path: `/api/v2/ad_hoc_commands/{id}/notifications/`

[Relaunch an Ad Hoc Command](op-api-v2-ad_hoc_commands-id-relaunch-get.html)
:   Method: get

    Path: `/api/v2/ad_hoc_commands/{id}/relaunch/`

[Relaunch an Ad Hoc Command](op-api-v2-ad_hoc_commands-id-relaunch-post.html)
:   Method: post

    Path: `/api/v2/ad_hoc_commands/{id}/relaunch/`

[Retrieve Ad Hoc Command Stdout](op-api-v2-ad_hoc_commands-id-stdout-get.html)
:   Method: get

    Path: `/api/v2/ad_hoc_commands/{id}/stdout/`

[Retrieve an Ad Hoc Command](op-api-v2-ad_hoc_commands-id-get.html)
:   Method: get

    Path: `/api/v2/ad_hoc_commands/{id}/`

[Retrieve an Ad Hoc Command](op-api-v2-ad_hoc_commands-id-cancel-get.html)
:   Method: get

    Path: `/api/v2/ad_hoc_commands/{id}/cancel/`

[Retrieve an Ad Hoc Command](op-api-v2-ad_hoc_commands-id-cancel-post.html)
:   Method: post

    Path: `/api/v2/ad_hoc_commands/{id}/cancel/`

Analytics

REST API endpoints for Analytics

[Analytics Adoption Rate Create](op-api-v2-analytics-adoption_rate-post.html)
:   Method: post

    Path: `/api/v2/analytics/adoption_rate/`

[Analytics Adoption Rate List](op-api-v2-analytics-adoption_rate-get.html)
:   Method: get

    Path: `/api/v2/analytics/adoption_rate/`

[Analytics Adoption Rate Options Create](op-api-v2-analytics-adoption_rate_options-post.html)
:   Method: post

    Path: `/api/v2/analytics/adoption_rate_options/`

[Analytics Adoption Rate Options List](op-api-v2-analytics-adoption_rate_options-get.html)
:   Method: get

    Path: `/api/v2/analytics/adoption_rate_options/`

[Analytics Authorized Create](op-api-v2-analytics-authorized-post.html)
:   Method: post

    Path: `/api/v2/analytics/authorized/`

[Analytics Authorized List](op-api-v2-analytics-authorized-get.html)
:   Method: get

    Path: `/api/v2/analytics/authorized/`

[Analytics Event Explorer Create](op-api-v2-analytics-event_explorer-post.html)
:   Method: post

    Path: `/api/v2/analytics/event_explorer/`

[Analytics Event Explorer List](op-api-v2-analytics-event_explorer-get.html)
:   Method: get

    Path: `/api/v2/analytics/event_explorer/`

[Analytics Event Explorer Options Create](op-api-v2-analytics-event_explorer_options-post.html)
:   Method: post

    Path: `/api/v2/analytics/event_explorer_options/`

[Analytics Event Explorer Options List](op-api-v2-analytics-event_explorer_options-get.html)
:   Method: get

    Path: `/api/v2/analytics/event_explorer_options/`

[Analytics Host Explorer Create](op-api-v2-analytics-host_explorer-post.html)
:   Method: post

    Path: `/api/v2/analytics/host_explorer/`

[Analytics Host Explorer List](op-api-v2-analytics-host_explorer-get.html)
:   Method: get

    Path: `/api/v2/analytics/host_explorer/`

[Analytics Host Explorer Options Create](op-api-v2-analytics-host_explorer_options-post.html)
:   Method: post

    Path: `/api/v2/analytics/host_explorer_options/`

[Analytics Host Explorer Options List](op-api-v2-analytics-host_explorer_options-get.html)
:   Method: get

    Path: `/api/v2/analytics/host_explorer_options/`

[Analytics Job Explorer Create](op-api-v2-analytics-job_explorer-post.html)
:   Method: post

    Path: `/api/v2/analytics/job_explorer/`

[Analytics Job Explorer List](op-api-v2-analytics-job_explorer-get.html)
:   Method: get

    Path: `/api/v2/analytics/job_explorer/`

[Analytics Job Explorer Options Create](op-api-v2-analytics-job_explorer_options-post.html)
:   Method: post

    Path: `/api/v2/analytics/job_explorer_options/`

[Analytics Job Explorer Options List](op-api-v2-analytics-job_explorer_options-get.html)
:   Method: get

    Path: `/api/v2/analytics/job_explorer_options/`

[Analytics List](op-api-v2-analytics-get.html)
:   Method: get

    Path: `/api/v2/analytics/`

[Analytics Probe Template for Hosts Create](op-api-v2-analytics-probe_template_for_hosts-post.html)
:   Method: post

    Path: `/api/v2/analytics/probe_template_for_hosts/`

[Analytics Probe Template for Hosts List](op-api-v2-analytics-probe_template_for_hosts-get.html)
:   Method: get

    Path: `/api/v2/analytics/probe_template_for_hosts/`

[Analytics Probe Template for Hosts Options Create](op-api-v2-analytics-probe_template_for_hosts_options-post.html)
:   Method: post

    Path: `/api/v2/analytics/probe_template_for_hosts_options/`

[Analytics Probe Template for Hosts Options List](op-api-v2-analytics-probe_template_for_hosts_options-get.html)
:   Method: get

    Path: `/api/v2/analytics/probe_template_for_hosts_options/`

[Analytics Probe Templates Create](op-api-v2-analytics-probe_templates-post.html)
:   Method: post

    Path: `/api/v2/analytics/probe_templates/`

[Analytics Probe Templates List](op-api-v2-analytics-probe_templates-get.html)
:   Method: get

    Path: `/api/v2/analytics/probe_templates/`

[Analytics Probe Templates Options Create](op-api-v2-analytics-probe_templates_options-post.html)
:   Method: post

    Path: `/api/v2/analytics/probe_templates_options/`

[Analytics Probe Templates Options List](op-api-v2-analytics-probe_templates_options-get.html)
:   Method: get

    Path: `/api/v2/analytics/probe_templates_options/`

[Analytics Report Create](op-api-v2-analytics-report-slug-post.html)
:   Method: post

    Path: `/api/v2/analytics/report/{slug}/`

[Analytics Report Options Create](op-api-v2-analytics-report_options-post.html)
:   Method: post

    Path: `/api/v2/analytics/report_options/`

[Analytics Report Options List](op-api-v2-analytics-report_options-get.html)
:   Method: get

    Path: `/api/v2/analytics/report_options/`

[Analytics Report Read](op-api-v2-analytics-report-slug-get.html)
:   Method: get

    Path: `/api/v2/analytics/report/{slug}/`

[Analytics Reports Create](op-api-v2-analytics-reports-post.html)
:   Method: post

    Path: `/api/v2/analytics/reports/`

[Analytics Reports List](op-api-v2-analytics-reports-get.html)
:   Method: get

    Path: `/api/v2/analytics/reports/`

[Analytics Roi Templates Create](op-api-v2-analytics-roi_templates-post.html)
:   Method: post

    Path: `/api/v2/analytics/roi_templates/`

[Analytics Roi Templates List](op-api-v2-analytics-roi_templates-get.html)
:   Method: get

    Path: `/api/v2/analytics/roi_templates/`

[Analytics Roi Templates Options Create](op-api-v2-analytics-roi_templates_options-post.html)
:   Method: post

    Path: `/api/v2/analytics/roi_templates_options/`

[Analytics Roi Templates Options List](op-api-v2-analytics-roi_templates_options-get.html)
:   Method: get

    Path: `/api/v2/analytics/roi_templates_options/`

Applications

REST API endpoints for Applications

[Create an Access Token for an Application](op-api-v2-applications-id-tokens-post.html)
:   Method: post

    Path: `/api/v2/applications/{id}/tokens/`

[Create an Application](op-api-v2-applications-post.html)
:   Method: post

    Path: `/api/v2/applications/`

[Delete an Application](op-api-v2-applications-id-delete.html)
:   Method: delete

    Path: `/api/v2/applications/{id}/`

[List Access Tokens for an Application](op-api-v2-applications-id-tokens-get.html)
:   Method: get

    Path: `/api/v2/applications/{id}/tokens/`

[List Activity Streams for an Application](op-api-v2-applications-id-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/applications/{id}/activity_stream/`

[List Applications](op-api-v2-applications-get.html)
:   Method: get

    Path: `/api/v2/applications/`

[Retrieve an Application](op-api-v2-applications-id-get.html)
:   Method: get

    Path: `/api/v2/applications/{id}/`

[Update an Application](op-api-v2-applications-id-patch.html)
:   Method: patch

    Path: `/api/v2/applications/{id}/`

[Update an Application](op-api-v2-applications-id-put.html)
:   Method: put

    Path: `/api/v2/applications/{id}/`

Auth

REST API endpoints for Auth

[Auth List](op-api-v2-auth-get.html)
:   Method: get

    Path: `/api/v2/auth/`

Bulk

REST API endpoints for Bulk

[Bulk Host Create](op-api-v2-bulk-host_create-get.html)
:   Method: get

    Path: `/api/v2/bulk/host_create/`

[Bulk Host Create](op-api-v2-bulk-host_create-post.html)
:   Method: post

    Path: `/api/v2/bulk/host_create/`

[Bulk Host Delete](op-api-v2-bulk-host_delete-get.html)
:   Method: get

    Path: `/api/v2/bulk/host_delete/`

[Bulk Host Delete](op-api-v2-bulk-host_delete-post.html)
:   Method: post

    Path: `/api/v2/bulk/host_delete/`

[Bulk Job Launch](op-api-v2-bulk-job_launch-get.html)
:   Method: get

    Path: `/api/v2/bulk/job_launch/`

[Bulk Job Launch](op-api-v2-bulk-job_launch-post.html)
:   Method: post

    Path: `/api/v2/bulk/job_launch/`

[Bulk List](op-api-v2-bulk-get.html)
:   Method: get

    Path: `/api/v2/bulk/`

Config

REST API endpoints for Config

[Config Attach Create](op-api-v2-config-attach-post.html)
:   Method: post

    Path: `/api/v2/config/attach/`

[Config List](op-api-v2-config-get.html)
:   Method: get

    Path: `/api/v2/config/`

[Config Subscriptions Create](op-api-v2-config-subscriptions-post.html)
:   Method: post

    Path: `/api/v2/config/subscriptions/`

[Delete an Existing License](op-api-v2-config-delete.html)
:   Method: delete

    Path: `/api/v2/config/`

[Install or Update an Existing License](op-api-v2-config-post.html)
:   Method: post

    Path: `/api/v2/config/`

Constructed Inventories

REST API endpoints for Constructed Inventories

[Create an Inventory](op-api-v2-constructed_inventories-post.html)
:   Method: post

    Path: `/api/v2/constructed_inventories/`

[Delete an Inventory](op-api-v2-constructed_inventories-id-delete.html)
:   Method: delete

    Path: `/api/v2/constructed_inventories/{id}/`

[List Inventories](op-api-v2-constructed_inventories-get.html)
:   Method: get

    Path: `/api/v2/constructed_inventories/`

[Retrieve an Inventory](op-api-v2-constructed_inventories-id-get.html)
:   Method: get

    Path: `/api/v2/constructed_inventories/{id}/`

[Update an Inventory](op-api-v2-constructed_inventories-id-patch.html)
:   Method: patch

    Path: `/api/v2/constructed_inventories/{id}/`

[Update an Inventory](op-api-v2-constructed_inventories-id-put.html)
:   Method: put

    Path: `/api/v2/constructed_inventories/{id}/`

Credential Input Sources

REST API endpoints for Credential Input Sources

[Create a Credential Input Source](op-api-v2-credential_input_sources-post.html)
:   Method: post

    Path: `/api/v2/credential_input_sources/`

[Delete a Credential Input Source](op-api-v2-credential_input_sources-id-delete.html)
:   Method: delete

    Path: `/api/v2/credential_input_sources/{id}/`

[List Credential Input Sources](op-api-v2-credential_input_sources-get.html)
:   Method: get

    Path: `/api/v2/credential_input_sources/`

[Retrieve a Credential Input Source](op-api-v2-credential_input_sources-id-get.html)
:   Method: get

    Path: `/api/v2/credential_input_sources/{id}/`

[Update a Credential Input Source](op-api-v2-credential_input_sources-id-patch.html)
:   Method: patch

    Path: `/api/v2/credential_input_sources/{id}/`

[Update a Credential Input Source](op-api-v2-credential_input_sources-id-put.html)
:   Method: put

    Path: `/api/v2/credential_input_sources/{id}/`

Credential Types

REST API endpoints for Credential Types

[Create a Credential for a Credential Type](op-api-v2-credential_types-id-credentials-post.html)
:   Method: post

    Path: `/api/v2/credential_types/{id}/credentials/`

[Create a Credential Type](op-api-v2-credential_types-post.html)
:   Method: post

    Path: `/api/v2/credential_types/`

[Delete a Credential Type](op-api-v2-credential_types-id-delete.html)
:   Method: delete

    Path: `/api/v2/credential_types/{id}/`

[List Activity Streams for a Credential Type](op-api-v2-credential_types-id-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/credential_types/{id}/activity_stream/`

[List Credential Types](op-api-v2-credential_types-get.html)
:   Method: get

    Path: `/api/v2/credential_types/`

[List Credentials for a Credential Type](op-api-v2-credential_types-id-credentials-get.html)
:   Method: get

    Path: `/api/v2/credential_types/{id}/credentials/`

[Retrieve a Credential Type](op-api-v2-credential_types-id-get.html)
:   Method: get

    Path: `/api/v2/credential_types/{id}/`

[Retrieve a Credential Type](op-api-v2-credential_types-id-test-get.html)
:   Method: get

    Path: `/api/v2/credential_types/{id}/test/`

[Retrieve a Credential Type](op-api-v2-credential_types-id-test-post.html)
:   Method: post

    Path: `/api/v2/credential_types/{id}/test/`

[Update a Credential Type](op-api-v2-credential_types-id-patch.html)
:   Method: patch

    Path: `/api/v2/credential_types/{id}/`

[Update a Credential Type](op-api-v2-credential_types-id-put.html)
:   Method: put

    Path: `/api/v2/credential_types/{id}/`

Credentials

REST API endpoints for Credentials

[Create a Credential](op-api-v2-credentials-post.html)
:   Method: post

    Path: `/api/v2/credentials/`

[Create a Credential Input Source for a Credential](op-api-v2-credentials-id-input_sources-post.html)
:   Method: post

    Path: `/api/v2/credentials/{id}/input_sources/`

[Credentials Copy Create](op-api-v2-credentials-id-copy-post.html)
:   Method: post

    Path: `/api/v2/credentials/{id}/copy/`

[Credentials Copy List](op-api-v2-credentials-id-copy-get.html)
:   Method: get

    Path: `/api/v2/credentials/{id}/copy/`

[Delete a Credential](op-api-v2-credentials-id-delete.html)
:   Method: delete

    Path: `/api/v2/credentials/{id}/`

[List Activity Streams for a Credential](op-api-v2-credentials-id-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/credentials/{id}/activity_stream/`

[List Credential Input Sources for a Credential](op-api-v2-credentials-id-input_sources-get.html)
:   Method: get

    Path: `/api/v2/credentials/{id}/input_sources/`

[List Credentials](op-api-v2-credentials-get.html)
:   Method: get

    Path: `/api/v2/credentials/`

[List Roles for a Credential](op-api-v2-credentials-id-object_roles-get.html)
:   Method: get

    Path: `/api/v2/credentials/{id}/object_roles/`

[List Teams for a Credential](op-api-v2-credentials-id-owner_teams-get.html)
:   Method: get

    Path: `/api/v2/credentials/{id}/owner_teams/`

[List Users](op-api-v2-credentials-id-access_list-get.html)
:   Method: get

    Path: `/api/v2/credentials/{id}/access_list/`

[List Users for a Credential](op-api-v2-credentials-id-owner_users-get.html)
:   Method: get

    Path: `/api/v2/credentials/{id}/owner_users/`

[Retrieve a Credential](op-api-v2-credentials-id-get.html)
:   Method: get

    Path: `/api/v2/credentials/{id}/`

[Retrieve a Credential](op-api-v2-credentials-id-test-get.html)
:   Method: get

    Path: `/api/v2/credentials/{id}/test/`

[Retrieve a Credential](op-api-v2-credentials-id-test-post.html)
:   Method: post

    Path: `/api/v2/credentials/{id}/test/`

[Update a Credential](op-api-v2-credentials-id-patch.html)
:   Method: patch

    Path: `/api/v2/credentials/{id}/`

[Update a Credential](op-api-v2-credentials-id-put.html)
:   Method: put

    Path: `/api/v2/credentials/{id}/`

Dashboard

REST API endpoints for Dashboard

[Dashboard List](op-api-v2-dashboard-get.html)
:   Method: get

    Path: `/api/v2/dashboard/`

[View Statistics for Job Runs](op-api-v2-dashboard-graphs-jobs-get.html)
:   Method: get

    Path: `/api/v2/dashboard/graphs/jobs/`

Dependency Manager

REST API endpoints for Dependency Manager

[Debug Dependency Manager List](op-api-debug-dependency_manager-get.html)
:   Method: get

    Path: `/api/debug/dependency_manager/`

Execution Environments

REST API endpoints for Execution Environments

[Create an Execution Environment](op-api-v2-execution_environments-post.html)
:   Method: post

    Path: `/api/v2/execution_environments/`

[Delete an Execution Environment](op-api-v2-execution_environments-id-delete.html)
:   Method: delete

    Path: `/api/v2/execution_environments/{id}/`

[Execution Environments Copy Create](op-api-v2-execution_environments-id-copy-post.html)
:   Method: post

    Path: `/api/v2/execution_environments/{id}/copy/`

[Execution Environments Copy List](op-api-v2-execution_environments-id-copy-get.html)
:   Method: get

    Path: `/api/v2/execution_environments/{id}/copy/`

[List Activity Streams for an Execution Environment](op-api-v2-execution_environments-id-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/execution_environments/{id}/activity_stream/`

[List Execution Environments](op-api-v2-execution_environments-get.html)
:   Method: get

    Path: `/api/v2/execution_environments/`

[List Unified Job Templates for an Execution Environment](op-api-v2-execution_environments-id-unified_job_templates-get.html)
:   Method: get

    Path: `/api/v2/execution_environments/{id}/unified_job_templates/`

[Retrieve an Execution Environment](op-api-v2-execution_environments-id-get.html)
:   Method: get

    Path: `/api/v2/execution_environments/{id}/`

[Update an Execution Environment](op-api-v2-execution_environments-id-patch.html)
:   Method: patch

    Path: `/api/v2/execution_environments/{id}/`

[Update an Execution Environment](op-api-v2-execution_environments-id-put.html)
:   Method: put

    Path: `/api/v2/execution_environments/{id}/`

Groups

REST API endpoints for Groups

[Create a Group](op-api-v2-groups-post.html)
:   Method: post

    Path: `/api/v2/groups/`

[Create a Group for a Group](op-api-v2-groups-id-children-post.html)
:   Method: post

    Path: `/api/v2/groups/{id}/children/`

[Create a Host for a Group](op-api-v2-groups-id-hosts-post.html)
:   Method: post

    Path: `/api/v2/groups/{id}/hosts/`

[Create an Ad Hoc Command for a Group](op-api-v2-groups-id-ad_hoc_commands-post.html)
:   Method: post

    Path: `/api/v2/groups/{id}/ad_hoc_commands/`

[Delete a Group](op-api-v2-groups-id-delete.html)
:   Method: delete

    Path: `/api/v2/groups/{id}/`

[List Activity Streams for a Group](op-api-v2-groups-id-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/groups/{id}/activity_stream/`

[List Ad Hoc Commands for a Group](op-api-v2-groups-id-ad_hoc_commands-get.html)
:   Method: get

    Path: `/api/v2/groups/{id}/ad_hoc_commands/`

[List All Hosts for a Group](op-api-v2-groups-id-all_hosts-get.html)
:   Method: get

    Path: `/api/v2/groups/{id}/all_hosts/`

[List Groups](op-api-v2-groups-get.html)
:   Method: get

    Path: `/api/v2/groups/`

[List Groups for a Group](op-api-v2-groups-id-children-get.html)
:   Method: get

    Path: `/api/v2/groups/{id}/children/`

[List Hosts for a Group](op-api-v2-groups-id-hosts-get.html)
:   Method: get

    Path: `/api/v2/groups/{id}/hosts/`

[List Inventory Sources for a Group](op-api-v2-groups-id-inventory_sources-get.html)
:   Method: get

    Path: `/api/v2/groups/{id}/inventory_sources/`

[List Job Events for a Group](op-api-v2-groups-id-job_events-get.html)
:   Method: get

    Path: `/api/v2/groups/{id}/job_events/`

[List Job Host Summaries for a Group](op-api-v2-groups-id-job_host_summaries-get.html)
:   Method: get

    Path: `/api/v2/groups/{id}/job_host_summaries/`

[List Potential Child Groups for a Group](op-api-v2-groups-id-potential_children-get.html)
:   Method: get

    Path: `/api/v2/groups/{id}/potential_children/`

[Retrieve a Group](op-api-v2-groups-id-get.html)
:   Method: get

    Path: `/api/v2/groups/{id}/`

[Retrieve Group Variable Data](op-api-v2-groups-id-variable_data-get.html)
:   Method: get

    Path: `/api/v2/groups/{id}/variable_data/`

[Update a Group](op-api-v2-groups-id-patch.html)
:   Method: patch

    Path: `/api/v2/groups/{id}/`

[Update a Group](op-api-v2-groups-id-put.html)
:   Method: put

    Path: `/api/v2/groups/{id}/`

[Update Group Variable Data](op-api-v2-groups-id-variable_data-patch.html)
:   Method: patch

    Path: `/api/v2/groups/{id}/variable_data/`

[Update Group Variable Data](op-api-v2-groups-id-variable_data-put.html)
:   Method: put

    Path: `/api/v2/groups/{id}/variable_data/`

Host Metric Summary Monthly

REST API endpoints for Host Metric Summary Monthly

[List Host Metric Summary Monthlys](op-api-v2-host_metric_summary_monthly-get.html)
:   Method: get

    Path: `/api/v2/host_metric_summary_monthly/`

Host Metrics

REST API endpoints for Host Metrics

[Delete a Host Metric](op-api-v2-host_metrics-id-delete.html)
:   Method: delete

    Path: `/api/v2/host_metrics/{id}/`

[List Host Metrics](op-api-v2-host_metrics-get.html)
:   Method: get

    Path: `/api/v2/host_metrics/`

[Retrieve a Host Metric](op-api-v2-host_metrics-id-get.html)
:   Method: get

    Path: `/api/v2/host_metrics/{id}/`

Hosts

REST API endpoints for Hosts

[Create a Group for a Host](op-api-v2-hosts-id-groups-post.html)
:   Method: post

    Path: `/api/v2/hosts/{id}/groups/`

[Create an Ad Hoc Command for a Host](op-api-v2-hosts-id-ad_hoc_commands-post.html)
:   Method: post

    Path: `/api/v2/hosts/{id}/ad_hoc_commands/`

[Delete a Host](op-api-v2-hosts-id-delete.html)
:   Method: delete

    Path: `/api/v2/hosts/{id}/`

[Hosts Create](op-api-v2-hosts-post.html)
:   Method: post

    Path: `/api/v2/hosts/`

[List Activity Streams for a Host](op-api-v2-hosts-id-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/hosts/{id}/activity_stream/`

[List Ad Hoc Command Events for a Host](op-api-v2-hosts-id-ad_hoc_command_events-get.html)
:   Method: get

    Path: `/api/v2/hosts/{id}/ad_hoc_command_events/`

[List Ad Hoc Commands for a Host](op-api-v2-hosts-id-ad_hoc_commands-get.html)
:   Method: get

    Path: `/api/v2/hosts/{id}/ad_hoc_commands/`

[List All Groups for a Host](op-api-v2-hosts-id-all_groups-get.html)
:   Method: get

    Path: `/api/v2/hosts/{id}/all_groups/`

[List Groups for a Host](op-api-v2-hosts-id-groups-get.html)
:   Method: get

    Path: `/api/v2/hosts/{id}/groups/`

[List Hosts](op-api-v2-hosts-get.html)
:   Method: get

    Path: `/api/v2/hosts/`

[List Inventories for a Host](op-api-v2-hosts-id-smart_inventories-get.html)
:   Method: get

    Path: `/api/v2/hosts/{id}/smart_inventories/`

[List Inventory Sources for a Host](op-api-v2-hosts-id-inventory_sources-get.html)
:   Method: get

    Path: `/api/v2/hosts/{id}/inventory_sources/`

[List Job Events for a Host](op-api-v2-hosts-id-job_events-get.html)
:   Method: get

    Path: `/api/v2/hosts/{id}/job_events/`

[List Job Host Summaries for a Host](op-api-v2-hosts-id-job_host_summaries-get.html)
:   Method: get

    Path: `/api/v2/hosts/{id}/job_host_summaries/`

[Retrieve a Host](op-api-v2-hosts-id-get.html)
:   Method: get

    Path: `/api/v2/hosts/{id}/`

[Retrieve a Host](op-api-v2-hosts-id-ansible_facts-get.html)
:   Method: get

    Path: `/api/v2/hosts/{id}/ansible_facts/`

[Retrieve Host Variable Data](op-api-v2-hosts-id-variable_data-get.html)
:   Method: get

    Path: `/api/v2/hosts/{id}/variable_data/`

[Update a Host](op-api-v2-hosts-id-patch.html)
:   Method: patch

    Path: `/api/v2/hosts/{id}/`

[Update a Host](op-api-v2-hosts-id-put.html)
:   Method: put

    Path: `/api/v2/hosts/{id}/`

[Update Host Variable Data](op-api-v2-hosts-id-variable_data-patch.html)
:   Method: patch

    Path: `/api/v2/hosts/{id}/variable_data/`

[Update Host Variable Data](op-api-v2-hosts-id-variable_data-put.html)
:   Method: put

    Path: `/api/v2/hosts/{id}/variable_data/`

Instance Groups

REST API endpoints for Instance Groups

[Create an Instance for an Instance Group](op-api-v2-instance_groups-id-instances-post.html)
:   Method: post

    Path: `/api/v2/instance_groups/{id}/instances/`

[Create an Instance Group](op-api-v2-instance_groups-post.html)
:   Method: post

    Path: `/api/v2/instance_groups/`

[Delete an Instance Group](op-api-v2-instance_groups-id-delete.html)
:   Method: delete

    Path: `/api/v2/instance_groups/{id}/`

[List Instance Groups](op-api-v2-instance_groups-get.html)
:   Method: get

    Path: `/api/v2/instance_groups/`

[List Instances for an Instance Group](op-api-v2-instance_groups-id-instances-get.html)
:   Method: get

    Path: `/api/v2/instance_groups/{id}/instances/`

[List Roles for an Instance Group](op-api-v2-instance_groups-id-object_roles-get.html)
:   Method: get

    Path: `/api/v2/instance_groups/{id}/object_roles/`

[List Unified Jobs for an Instance Group](op-api-v2-instance_groups-id-jobs-get.html)
:   Method: get

    Path: `/api/v2/instance_groups/{id}/jobs/`

[List Users](op-api-v2-instance_groups-id-access_list-get.html)
:   Method: get

    Path: `/api/v2/instance_groups/{id}/access_list/`

[Retrieve an Instance Group](op-api-v2-instance_groups-id-get.html)
:   Method: get

    Path: `/api/v2/instance_groups/{id}/`

[Update an Instance Group](op-api-v2-instance_groups-id-patch.html)
:   Method: patch

    Path: `/api/v2/instance_groups/{id}/`

[Update an Instance Group](op-api-v2-instance_groups-id-put.html)
:   Method: put

    Path: `/api/v2/instance_groups/{id}/`

Instances

REST API endpoints for Instances

[Create an Instance](op-api-v2-instances-post.html)
:   Method: post

    Path: `/api/v2/instances/`

[Create an Instance Group for an Instance](op-api-v2-instances-id-instance_groups-post.html)
:   Method: post

    Path: `/api/v2/instances/{id}/instance_groups/`

[Health Check Data](op-api-v2-instances-id-health_check-get.html)
:   Method: get

    Path: `/api/v2/instances/{id}/health_check/`

[Instances Health Check Create](op-api-v2-instances-id-health_check-post.html)
:   Method: post

    Path: `/api/v2/instances/{id}/health_check/`

[Instances Install Bundle List](op-api-v2-instances-id-install_bundle-get.html)
:   Method: get

    Path: `/api/v2/instances/{id}/install_bundle/`

[List Instance Groups for an Instance](op-api-v2-instances-id-instance_groups-get.html)
:   Method: get

    Path: `/api/v2/instances/{id}/instance_groups/`

[List Instances](op-api-v2-instances-get.html)
:   Method: get

    Path: `/api/v2/instances/`

[List Instances for an Instance](op-api-v2-instances-id-peers-get.html)
:   Method: get

    Path: `/api/v2/instances/{id}/peers/`

[List Unified Jobs for an Instance](op-api-v2-instances-id-jobs-get.html)
:   Method: get

    Path: `/api/v2/instances/{id}/jobs/`

[Retrieve an Instance](op-api-v2-instances-id-get.html)
:   Method: get

    Path: `/api/v2/instances/{id}/`

[Update an Instance](op-api-v2-instances-id-patch.html)
:   Method: patch

    Path: `/api/v2/instances/{id}/`

[Update an Instance](op-api-v2-instances-id-put.html)
:   Method: put

    Path: `/api/v2/instances/{id}/`

Inventories

REST API endpoints for Inventories

[Create a Group for an Inventory](op-api-v2-inventories-id-groups-post.html)
:   Method: post

    Path: `/api/v2/inventories/{id}/groups/`

[Create a Host for an Inventory](op-api-v2-inventories-id-hosts-post.html)
:   Method: post

    Path: `/api/v2/inventories/{id}/hosts/`

[Create a Label for an Inventory](op-api-v2-inventories-id-labels-post.html)
:   Method: post

    Path: `/api/v2/inventories/{id}/labels/`

[Create an Ad Hoc Command for an Inventory](op-api-v2-inventories-id-ad_hoc_commands-post.html)
:   Method: post

    Path: `/api/v2/inventories/{id}/ad_hoc_commands/`

[Create an Instance Group for an Inventory](op-api-v2-inventories-id-instance_groups-post.html)
:   Method: post

    Path: `/api/v2/inventories/{id}/instance_groups/`

[Create an Inventory](op-api-v2-inventories-post.html)
:   Method: post

    Path: `/api/v2/inventories/`

[Create an Inventory for an Inventory](op-api-v2-inventories-id-input_inventories-post.html)
:   Method: post

    Path: `/api/v2/inventories/{id}/input_inventories/`

[Create an Inventory Source for an Inventory](op-api-v2-inventories-id-inventory_sources-post.html)
:   Method: post

    Path: `/api/v2/inventories/{id}/inventory_sources/`

[Delete an Inventory](op-api-v2-inventories-id-delete.html)
:   Method: delete

    Path: `/api/v2/inventories/{id}/`

[Generate Inventory Group and Host Data as Needed for an Inventory Script.](op-api-v2-inventories-id-script-get.html)
:   Method: get

    Path: `/api/v2/inventories/{id}/script/`

[Group Tree for an Inventory](op-api-v2-inventories-id-tree-get.html)
:   Method: get

    Path: `/api/v2/inventories/{id}/tree/`

[Inventories Copy Create](op-api-v2-inventories-id-copy-post.html)
:   Method: post

    Path: `/api/v2/inventories/{id}/copy/`

[Inventories Copy List](op-api-v2-inventories-id-copy-get.html)
:   Method: get

    Path: `/api/v2/inventories/{id}/copy/`

[Inventories Root Groups Create](op-api-v2-inventories-id-root_groups-post.html)
:   Method: post

    Path: `/api/v2/inventories/{id}/root_groups/`

[List Activity Streams for an Inventory](op-api-v2-inventories-id-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/inventories/{id}/activity_stream/`

[List Ad Hoc Commands for an Inventory](op-api-v2-inventories-id-ad_hoc_commands-get.html)
:   Method: get

    Path: `/api/v2/inventories/{id}/ad_hoc_commands/`

[List Groups for an Inventory](op-api-v2-inventories-id-groups-get.html)
:   Method: get

    Path: `/api/v2/inventories/{id}/groups/`

[List Hosts for an Inventory](op-api-v2-inventories-id-hosts-get.html)
:   Method: get

    Path: `/api/v2/inventories/{id}/hosts/`

[List Instance Groups for an Inventory](op-api-v2-inventories-id-instance_groups-get.html)
:   Method: get

    Path: `/api/v2/inventories/{id}/instance_groups/`

[List Inventories](op-api-v2-inventories-get.html)
:   Method: get

    Path: `/api/v2/inventories/`

[List Inventories for an Inventory](op-api-v2-inventories-id-input_inventories-get.html)
:   Method: get

    Path: `/api/v2/inventories/{id}/input_inventories/`

[List Inventory Sources for an Inventory](op-api-v2-inventories-id-inventory_sources-get.html)
:   Method: get

    Path: `/api/v2/inventories/{id}/inventory_sources/`

[List Job Templates for an Inventory](op-api-v2-inventories-id-job_templates-get.html)
:   Method: get

    Path: `/api/v2/inventories/{id}/job_templates/`

[List Labels for an Inventory](op-api-v2-inventories-id-labels-get.html)
:   Method: get

    Path: `/api/v2/inventories/{id}/labels/`

[List Roles for an Inventory](op-api-v2-inventories-id-object_roles-get.html)
:   Method: get

    Path: `/api/v2/inventories/{id}/object_roles/`

[List Root Groups for an Inventory](op-api-v2-inventories-id-root_groups-get.html)
:   Method: get

    Path: `/api/v2/inventories/{id}/root_groups/`

[List Users](op-api-v2-inventories-id-access_list-get.html)
:   Method: get

    Path: `/api/v2/inventories/{id}/access_list/`

[Retrieve an Inventory](op-api-v2-inventories-id-get.html)
:   Method: get

    Path: `/api/v2/inventories/{id}/`

[Retrieve Inventory Variable Data](op-api-v2-inventories-id-variable_data-get.html)
:   Method: get

    Path: `/api/v2/inventories/{id}/variable_data/`

[Update an Inventory](op-api-v2-inventories-id-patch.html)
:   Method: patch

    Path: `/api/v2/inventories/{id}/`

[Update an Inventory](op-api-v2-inventories-id-put.html)
:   Method: put

    Path: `/api/v2/inventories/{id}/`

[Update Inventory Sources](op-api-v2-inventories-id-update_inventory_sources-get.html)
:   Method: get

    Path: `/api/v2/inventories/{id}/update_inventory_sources/`

[Update Inventory Sources](op-api-v2-inventories-id-update_inventory_sources-post.html)
:   Method: post

    Path: `/api/v2/inventories/{id}/update_inventory_sources/`

[Update Inventory Variable Data](op-api-v2-inventories-id-variable_data-patch.html)
:   Method: patch

    Path: `/api/v2/inventories/{id}/variable_data/`

[Update Inventory Variable Data](op-api-v2-inventories-id-variable_data-put.html)
:   Method: put

    Path: `/api/v2/inventories/{id}/variable_data/`

Inventory Sources

REST API endpoints for Inventory Sources

[Create a Credential for an Inventory Source](op-api-v2-inventory_sources-id-credentials-post.html)
:   Method: post

    Path: `/api/v2/inventory_sources/{id}/credentials/`

[Create a Group for an Inventory Source](op-api-v2-inventory_sources-id-groups-delete.html)
:   Method: delete

    Path: `/api/v2/inventory_sources/{id}/groups/`

[Create a Host for an Inventory Source](op-api-v2-inventory_sources-id-hosts-delete.html)
:   Method: delete

    Path: `/api/v2/inventory_sources/{id}/hosts/`

[Create a Notification Template for an Inventory Source](op-api-v2-inventory_sources-id-notification_templates_error-post.html)
:   Method: post

    Path: `/api/v2/inventory_sources/{id}/notification_templates_error/`

[Create a Notification Template for an Inventory Source](op-api-v2-inventory_sources-id-notification_templates_started-post.html)
:   Method: post

    Path: `/api/v2/inventory_sources/{id}/notification_templates_started/`

[Create a Notification Template for an Inventory Source](op-api-v2-inventory_sources-id-notification_templates_success-post.html)
:   Method: post

    Path: `/api/v2/inventory_sources/{id}/notification_templates_success/`

[Create a Schedule for an Inventory Source](op-api-v2-inventory_sources-id-schedules-post.html)
:   Method: post

    Path: `/api/v2/inventory_sources/{id}/schedules/`

[Create an Inventory Source](op-api-v2-inventory_sources-post.html)
:   Method: post

    Path: `/api/v2/inventory_sources/`

[Delete an Inventory Source](op-api-v2-inventory_sources-id-delete.html)
:   Method: delete

    Path: `/api/v2/inventory_sources/{id}/`

[List Activity Streams for an Inventory Source](op-api-v2-inventory_sources-id-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/inventory_sources/{id}/activity_stream/`

[List Credentials for an Inventory Source](op-api-v2-inventory_sources-id-credentials-get.html)
:   Method: get

    Path: `/api/v2/inventory_sources/{id}/credentials/`

[List Groups for an Inventory Source](op-api-v2-inventory_sources-id-groups-get.html)
:   Method: get

    Path: `/api/v2/inventory_sources/{id}/groups/`

[List Hosts for an Inventory Source](op-api-v2-inventory_sources-id-hosts-get.html)
:   Method: get

    Path: `/api/v2/inventory_sources/{id}/hosts/`

[List Inventory Sources](op-api-v2-inventory_sources-get.html)
:   Method: get

    Path: `/api/v2/inventory_sources/`

[List Inventory Updates for an Inventory Source](op-api-v2-inventory_sources-id-inventory_updates-get.html)
:   Method: get

    Path: `/api/v2/inventory_sources/{id}/inventory_updates/`

[List Notification Templates for an Inventory Source](op-api-v2-inventory_sources-id-notification_templates_error-get.html)
:   Method: get

    Path: `/api/v2/inventory_sources/{id}/notification_templates_error/`

[List Notification Templates for an Inventory Source](op-api-v2-inventory_sources-id-notification_templates_started-get.html)
:   Method: get

    Path: `/api/v2/inventory_sources/{id}/notification_templates_started/`

[List Notification Templates for an Inventory Source](op-api-v2-inventory_sources-id-notification_templates_success-get.html)
:   Method: get

    Path: `/api/v2/inventory_sources/{id}/notification_templates_success/`

[List Schedules for an Inventory Source](op-api-v2-inventory_sources-id-schedules-get.html)
:   Method: get

    Path: `/api/v2/inventory_sources/{id}/schedules/`

[Retrieve an Inventory Source](op-api-v2-inventory_sources-id-get.html)
:   Method: get

    Path: `/api/v2/inventory_sources/{id}/`

[Update an Inventory Source](op-api-v2-inventory_sources-id-patch.html)
:   Method: patch

    Path: `/api/v2/inventory_sources/{id}/`

[Update an Inventory Source](op-api-v2-inventory_sources-id-put.html)
:   Method: put

    Path: `/api/v2/inventory_sources/{id}/`

[Update Inventory Source](op-api-v2-inventory_sources-id-update-get.html)
:   Method: get

    Path: `/api/v2/inventory_sources/{id}/update/`

[Update Inventory Source](op-api-v2-inventory_sources-id-update-post.html)
:   Method: post

    Path: `/api/v2/inventory_sources/{id}/update/`

Inventory Updates

REST API endpoints for Inventory Updates

[Delete an Inventory Update](op-api-v2-inventory_updates-id-delete.html)
:   Method: delete

    Path: `/api/v2/inventory_updates/{id}/`

[List Credentials for an Inventory Update](op-api-v2-inventory_updates-id-credentials-get.html)
:   Method: get

    Path: `/api/v2/inventory_updates/{id}/credentials/`

[List Inventory Update Events for an Inventory Update](op-api-v2-inventory_updates-id-events-get.html)
:   Method: get

    Path: `/api/v2/inventory_updates/{id}/events/`

[List Inventory Updates](op-api-v2-inventory_updates-get.html)
:   Method: get

    Path: `/api/v2/inventory_updates/`

[List Notifications for an Inventory Update](op-api-v2-inventory_updates-id-notifications-get.html)
:   Method: get

    Path: `/api/v2/inventory_updates/{id}/notifications/`

[Retrieve an Inventory Update](op-api-v2-inventory_updates-id-get.html)
:   Method: get

    Path: `/api/v2/inventory_updates/{id}/`

[Retrieve an Inventory Update](op-api-v2-inventory_updates-id-cancel-get.html)
:   Method: get

    Path: `/api/v2/inventory_updates/{id}/cancel/`

[Retrieve an Inventory Update](op-api-v2-inventory_updates-id-cancel-post.html)
:   Method: post

    Path: `/api/v2/inventory_updates/{id}/cancel/`

[Retrieve Inventory Update Stdout](op-api-v2-inventory_updates-id-stdout-get.html)
:   Method: get

    Path: `/api/v2/inventory_updates/{id}/stdout/`

Job Events

REST API endpoints for Job Events

[List Job Events for a Job Event](op-api-v2-job_events-id-children-get.html)
:   Method: get

    Path: `/api/v2/job_events/{id}/children/`

[Retrieve a Job Event](op-api-v2-job_events-id-get.html)
:   Method: get

    Path: `/api/v2/job_events/{id}/`

Job Host Summaries

REST API endpoints for Job Host Summaries

[Retrieve a Job Host Summary](op-api-v2-job_host_summaries-id-get.html)
:   Method: get

    Path: `/api/v2/job_host_summaries/{id}/`

Job Templates

REST API endpoints for Job Templates

[Create a Credential for a Job Template](op-api-v2-job_templates-id-credentials-post.html)
:   Method: post

    Path: `/api/v2/job_templates/{id}/credentials/`

[Create a Job Template](op-api-v2-job_templates-post.html)
:   Method: post

    Path: `/api/v2/job_templates/`

[Create a Label for a Job Template](op-api-v2-job_templates-id-labels-post.html)
:   Method: post

    Path: `/api/v2/job_templates/{id}/labels/`

[Create a Notification Template for a Job Template](op-api-v2-job_templates-id-notification_templates_error-post.html)
:   Method: post

    Path: `/api/v2/job_templates/{id}/notification_templates_error/`

[Create a Notification Template for a Job Template](op-api-v2-job_templates-id-notification_templates_started-post.html)
:   Method: post

    Path: `/api/v2/job_templates/{id}/notification_templates_started/`

[Create a Notification Template for a Job Template](op-api-v2-job_templates-id-notification_templates_success-post.html)
:   Method: post

    Path: `/api/v2/job_templates/{id}/notification_templates_success/`

[Create a Schedule for a Job Template](op-api-v2-job_templates-id-schedules-post.html)
:   Method: post

    Path: `/api/v2/job_templates/{id}/schedules/`

[Create a Workflow Job for a Job Template](op-api-v2-job_templates-id-slice_workflow_jobs-post.html)
:   Method: post

    Path: `/api/v2/job_templates/{id}/slice_workflow_jobs/`

[Create an Instance Group for a Job Template](op-api-v2-job_templates-id-instance_groups-post.html)
:   Method: post

    Path: `/api/v2/job_templates/{id}/instance_groups/`

[Delete a Job Template](op-api-v2-job_templates-id-delete.html)
:   Method: delete

    Path: `/api/v2/job_templates/{id}/`

[Job Templates Bitbucket Dc Create](op-api-v2-job_templates-id-bitbucket_dc-post.html)
:   Method: post

    Path: `/api/v2/job_templates/{id}/bitbucket_dc/`

[Job Templates Copy Create](op-api-v2-job_templates-id-copy-post.html)
:   Method: post

    Path: `/api/v2/job_templates/{id}/copy/`

[Job Templates Copy List](op-api-v2-job_templates-id-copy-get.html)
:   Method: get

    Path: `/api/v2/job_templates/{id}/copy/`

[Job Templates Github Create](op-api-v2-job_templates-id-github-post.html)
:   Method: post

    Path: `/api/v2/job_templates/{id}/github/`

[Job Templates Gitlab Create](op-api-v2-job_templates-id-gitlab-post.html)
:   Method: post

    Path: `/api/v2/job_templates/{id}/gitlab/`

[Job Templates Webhook Key Create](op-api-v2-job_templates-id-webhook_key-post.html)
:   Method: post

    Path: `/api/v2/job_templates/{id}/webhook_key/`

[Job Templates Webhook Key List](op-api-v2-job_templates-id-webhook_key-get.html)
:   Method: get

    Path: `/api/v2/job_templates/{id}/webhook_key/`

[Launch a Job Template](op-api-v2-job_templates-id-launch-get.html)
:   Method: get

    Path: `/api/v2/job_templates/{id}/launch/`

[Launch a Job Template](op-api-v2-job_templates-id-launch-post.html)
:   Method: post

    Path: `/api/v2/job_templates/{id}/launch/`

[List Activity Streams for a Job Template](op-api-v2-job_templates-id-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/job_templates/{id}/activity_stream/`

[List Credentials for a Job Template](op-api-v2-job_templates-id-credentials-get.html)
:   Method: get

    Path: `/api/v2/job_templates/{id}/credentials/`

[List Instance Groups for a Job Template](op-api-v2-job_templates-id-instance_groups-get.html)
:   Method: get

    Path: `/api/v2/job_templates/{id}/instance_groups/`

[List Job Templates](op-api-v2-job_templates-get.html)
:   Method: get

    Path: `/api/v2/job_templates/`

[List Jobs for a Job Template](op-api-v2-job_templates-id-jobs-get.html)
:   Method: get

    Path: `/api/v2/job_templates/{id}/jobs/`

[List Labels for a Job Template](op-api-v2-job_templates-id-labels-get.html)
:   Method: get

    Path: `/api/v2/job_templates/{id}/labels/`

[List Notification Templates for a Job Template](op-api-v2-job_templates-id-notification_templates_error-get.html)
:   Method: get

    Path: `/api/v2/job_templates/{id}/notification_templates_error/`

[List Notification Templates for a Job Template](op-api-v2-job_templates-id-notification_templates_started-get.html)
:   Method: get

    Path: `/api/v2/job_templates/{id}/notification_templates_started/`

[List Notification Templates for a Job Template](op-api-v2-job_templates-id-notification_templates_success-get.html)
:   Method: get

    Path: `/api/v2/job_templates/{id}/notification_templates_success/`

[List Roles for a Job Template](op-api-v2-job_templates-id-object_roles-get.html)
:   Method: get

    Path: `/api/v2/job_templates/{id}/object_roles/`

[List Schedules for a Job Template](op-api-v2-job_templates-id-schedules-get.html)
:   Method: get

    Path: `/api/v2/job_templates/{id}/schedules/`

[List Users](op-api-v2-job_templates-id-access_list-get.html)
:   Method: get

    Path: `/api/v2/job_templates/{id}/access_list/`

[List Workflow Jobs for a Job Template](op-api-v2-job_templates-id-slice_workflow_jobs-get.html)
:   Method: get

    Path: `/api/v2/job_templates/{id}/slice_workflow_jobs/`

[POST Requests to This Resource Should Include the Full Specification for a Job Template's Survey](op-api-v2-job_templates-id-survey_spec-delete.html)
:   Method: delete

    Path: `/api/v2/job_templates/{id}/survey_spec/`

[POST Requests to This Resource Should Include the Full Specification for a Job Template's Survey](op-api-v2-job_templates-id-survey_spec-get.html)
:   Method: get

    Path: `/api/v2/job_templates/{id}/survey_spec/`

[POST Requests to This Resource Should Include the Full Specification for a Job Template's Survey](op-api-v2-job_templates-id-survey_spec-post.html)
:   Method: post

    Path: `/api/v2/job_templates/{id}/survey_spec/`

[Retrieve a Job Template](op-api-v2-job_templates-id-get.html)
:   Method: get

    Path: `/api/v2/job_templates/{id}/`

[The Job Template Callback Allows for Ephemeral Hosts to Launch a New Job.](op-api-v2-job_templates-id-callback-get.html)
:   Method: get

    Path: `/api/v2/job_templates/{id}/callback/`

[The Job Template Callback Allows for Ephemeral Hosts to Launch a New Job.](op-api-v2-job_templates-id-callback-post.html)
:   Method: post

    Path: `/api/v2/job_templates/{id}/callback/`

[Update a Job Template](op-api-v2-job_templates-id-patch.html)
:   Method: patch

    Path: `/api/v2/job_templates/{id}/`

[Update a Job Template](op-api-v2-job_templates-id-put.html)
:   Method: put

    Path: `/api/v2/job_templates/{id}/`

Jobs

REST API endpoints for Jobs

[Create a Schedule Based on a Job](op-api-v2-jobs-id-create_schedule-get.html)
:   Method: get

    Path: `/api/v2/jobs/{id}/create_schedule/`

[Create a Schedule Based on a Job](op-api-v2-jobs-id-create_schedule-post.html)
:   Method: post

    Path: `/api/v2/jobs/{id}/create_schedule/`

[Delete a Job](op-api-v2-jobs-id-delete.html)
:   Method: delete

    Path: `/api/v2/jobs/{id}/`

[Determine if a Job Can Be Canceled](op-api-v2-jobs-id-cancel-get.html)
:   Method: get

    Path: `/api/v2/jobs/{id}/cancel/`

[Jobs Cancel Create](op-api-v2-jobs-id-cancel-post.html)
:   Method: post

    Path: `/api/v2/jobs/{id}/cancel/`

[List Activity Streams for a Job](op-api-v2-jobs-id-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/jobs/{id}/activity_stream/`

[List Credentials for a Job](op-api-v2-jobs-id-credentials-get.html)
:   Method: get

    Path: `/api/v2/jobs/{id}/credentials/`

[List Job Events for a Job](op-api-v2-jobs-id-job_events-get.html)
:   Method: get

    Path: `/api/v2/jobs/{id}/job_events/`

[List Job Host Summaries for a Job](op-api-v2-jobs-id-job_host_summaries-get.html)
:   Method: get

    Path: `/api/v2/jobs/{id}/job_host_summaries/`

[List Jobs](op-api-v2-jobs-get.html)
:   Method: get

    Path: `/api/v2/jobs/`

[List Labels for a Job](op-api-v2-jobs-id-labels-get.html)
:   Method: get

    Path: `/api/v2/jobs/{id}/labels/`

[List Notifications for a Job](op-api-v2-jobs-id-notifications-get.html)
:   Method: get

    Path: `/api/v2/jobs/{id}/notifications/`

[Relaunch a Job](op-api-v2-jobs-id-relaunch-get.html)
:   Method: get

    Path: `/api/v2/jobs/{id}/relaunch/`

[Relaunch a Job](op-api-v2-jobs-id-relaunch-post.html)
:   Method: post

    Path: `/api/v2/jobs/{id}/relaunch/`

[Retrieve a Job](op-api-v2-jobs-id-get.html)
:   Method: get

    Path: `/api/v2/jobs/{id}/`

[Retrieve Job Stdout](op-api-v2-jobs-id-stdout-get.html)
:   Method: get

    Path: `/api/v2/jobs/{id}/stdout/`

[View a Summary of Children Events](op-api-v2-jobs-id-job_events-children_summary-get.html)
:   Method: get

    Path: `/api/v2/jobs/{id}/job_events/children_summary/`

Labels

REST API endpoints for Labels

[Create a Label](op-api-v2-labels-post.html)
:   Method: post

    Path: `/api/v2/labels/`

[List Labels](op-api-v2-labels-get.html)
:   Method: get

    Path: `/api/v2/labels/`

[Retrieve a Label](op-api-v2-labels-id-get.html)
:   Method: get

    Path: `/api/v2/labels/{id}/`

[Update a Label](op-api-v2-labels-id-patch.html)
:   Method: patch

    Path: `/api/v2/labels/{id}/`

[Update a Label](op-api-v2-labels-id-put.html)
:   Method: put

    Path: `/api/v2/labels/{id}/`

Me

REST API endpoints for Me

[Retrieve Information About the Current User](op-api-v2-me-get.html)
:   Method: get

    Path: `/api/v2/me/`

Mesh Visualizer

REST API endpoints for Mesh Visualizer

[Mesh Visualizer List](op-api-v2-mesh_visualizer-get.html)
:   Method: get

    Path: `/api/v2/mesh_visualizer/`

Metrics

REST API endpoints for Metrics

[Metrics List](op-api-v2-metrics-get.html)
:   Method: get

    Path: `/api/v2/metrics/`

Notification Templates

REST API endpoints for Notification Templates

[Create a Notification Template](op-api-v2-notification_templates-post.html)
:   Method: post

    Path: `/api/v2/notification_templates/`

[Delete a Notification Template](op-api-v2-notification_templates-id-delete.html)
:   Method: delete

    Path: `/api/v2/notification_templates/{id}/`

[List Notification Templates](op-api-v2-notification_templates-get.html)
:   Method: get

    Path: `/api/v2/notification_templates/`

[List Notifications for a Notification Template](op-api-v2-notification_templates-id-notifications-get.html)
:   Method: get

    Path: `/api/v2/notification_templates/{id}/notifications/`

[Notification Templates Copy Create](op-api-v2-notification_templates-id-copy-post.html)
:   Method: post

    Path: `/api/v2/notification_templates/{id}/copy/`

[Notification Templates Copy List](op-api-v2-notification_templates-id-copy-get.html)
:   Method: get

    Path: `/api/v2/notification_templates/{id}/copy/`

[Notification Templates Test Create](op-api-v2-notification_templates-id-test-post.html)
:   Method: post

    Path: `/api/v2/notification_templates/{id}/test/`

[Retrieve a Notification Template](op-api-v2-notification_templates-id-get.html)
:   Method: get

    Path: `/api/v2/notification_templates/{id}/`

[Update a Notification Template](op-api-v2-notification_templates-id-patch.html)
:   Method: patch

    Path: `/api/v2/notification_templates/{id}/`

[Update a Notification Template](op-api-v2-notification_templates-id-put.html)
:   Method: put

    Path: `/api/v2/notification_templates/{id}/`

Notifications

REST API endpoints for Notifications

[List Notifications](op-api-v2-notifications-get.html)
:   Method: get

    Path: `/api/v2/notifications/`

[Retrieve a Notification](op-api-v2-notifications-id-get.html)
:   Method: get

    Path: `/api/v2/notifications/{id}/`

Organizations

REST API endpoints for Organizations

[Create a Credential for an Organization](op-api-v2-organizations-id-credentials-post.html)
:   Method: post

    Path: `/api/v2/organizations/{id}/credentials/`

[Create a Credential for an Organization](op-api-v2-organizations-id-galaxy_credentials-post.html)
:   Method: post

    Path: `/api/v2/organizations/{id}/galaxy_credentials/`

[Create a Job Template for an Organization](op-api-v2-organizations-id-job_templates-post.html)
:   Method: post

    Path: `/api/v2/organizations/{id}/job_templates/`

[Create a Notification Template for an Organization](op-api-v2-organizations-id-notification_templates-post.html)
:   Method: post

    Path: `/api/v2/organizations/{id}/notification_templates/`

[Create a Notification Template for an Organization](op-api-v2-organizations-id-notification_templates_approvals-post.html)
:   Method: post

    Path: `/api/v2/organizations/{id}/notification_templates_approvals/`

[Create a Notification Template for an Organization](op-api-v2-organizations-id-notification_templates_error-post.html)
:   Method: post

    Path: `/api/v2/organizations/{id}/notification_templates_error/`

[Create a Notification Template for an Organization](op-api-v2-organizations-id-notification_templates_started-post.html)
:   Method: post

    Path: `/api/v2/organizations/{id}/notification_templates_started/`

[Create a Notification Template for an Organization](op-api-v2-organizations-id-notification_templates_success-post.html)
:   Method: post

    Path: `/api/v2/organizations/{id}/notification_templates_success/`

[Create a Project for an Organization](op-api-v2-organizations-id-projects-post.html)
:   Method: post

    Path: `/api/v2/organizations/{id}/projects/`

[Create a Team for an Organization](op-api-v2-organizations-id-teams-post.html)
:   Method: post

    Path: `/api/v2/organizations/{id}/teams/`

[Create a User for an Organization](op-api-v2-organizations-id-users-post.html)
:   Method: post

    Path: `/api/v2/organizations/{id}/users/`

[Create a Workflow Job Template for an Organization](op-api-v2-organizations-id-workflow_job_templates-post.html)
:   Method: post

    Path: `/api/v2/organizations/{id}/workflow_job_templates/`

[Create an Admin User for an Organization](op-api-v2-organizations-id-admins-post.html)
:   Method: post

    Path: `/api/v2/organizations/{id}/admins/`

[Create an Application for an Organization](op-api-v2-organizations-id-applications-post.html)
:   Method: post

    Path: `/api/v2/organizations/{id}/applications/`

[Create an Execution Environment for an Organization](op-api-v2-organizations-id-execution_environments-post.html)
:   Method: post

    Path: `/api/v2/organizations/{id}/execution_environments/`

[Create an Instance Group for an Organization](op-api-v2-organizations-id-instance_groups-post.html)
:   Method: post

    Path: `/api/v2/organizations/{id}/instance_groups/`

[Create an Organization](op-api-v2-organizations-post.html)
:   Method: post

    Path: `/api/v2/organizations/`

[Delete an Organization](op-api-v2-organizations-id-delete.html)
:   Method: delete

    Path: `/api/v2/organizations/{id}/`

[List Activity Streams for an Organization](op-api-v2-organizations-id-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/organizations/{id}/activity_stream/`

[List Admin Users for an Organization](op-api-v2-organizations-id-admins-get.html)
:   Method: get

    Path: `/api/v2/organizations/{id}/admins/`

[List Applications for an Organization](op-api-v2-organizations-id-applications-get.html)
:   Method: get

    Path: `/api/v2/organizations/{id}/applications/`

[List Credentials for an Organization](op-api-v2-organizations-id-credentials-get.html)
:   Method: get

    Path: `/api/v2/organizations/{id}/credentials/`

[List Credentials for an Organization](op-api-v2-organizations-id-galaxy_credentials-get.html)
:   Method: get

    Path: `/api/v2/organizations/{id}/galaxy_credentials/`

[List Execution Environments for an Organization](op-api-v2-organizations-id-execution_environments-get.html)
:   Method: get

    Path: `/api/v2/organizations/{id}/execution_environments/`

[List Instance Groups for an Organization](op-api-v2-organizations-id-instance_groups-get.html)
:   Method: get

    Path: `/api/v2/organizations/{id}/instance_groups/`

[List Inventories for an Organization](op-api-v2-organizations-id-inventories-get.html)
:   Method: get

    Path: `/api/v2/organizations/{id}/inventories/`

[List Job Templates for an Organization](op-api-v2-organizations-id-job_templates-get.html)
:   Method: get

    Path: `/api/v2/organizations/{id}/job_templates/`

[List Notification Templates for an Organization](op-api-v2-organizations-id-notification_templates-get.html)
:   Method: get

    Path: `/api/v2/organizations/{id}/notification_templates/`

[List Notification Templates for an Organization](op-api-v2-organizations-id-notification_templates_approvals-get.html)
:   Method: get

    Path: `/api/v2/organizations/{id}/notification_templates_approvals/`

[List Notification Templates for an Organization](op-api-v2-organizations-id-notification_templates_error-get.html)
:   Method: get

    Path: `/api/v2/organizations/{id}/notification_templates_error/`

[List Notification Templates for an Organization](op-api-v2-organizations-id-notification_templates_started-get.html)
:   Method: get

    Path: `/api/v2/organizations/{id}/notification_templates_started/`

[List Notification Templates for an Organization](op-api-v2-organizations-id-notification_templates_success-get.html)
:   Method: get

    Path: `/api/v2/organizations/{id}/notification_templates_success/`

[List Organizations](op-api-v2-organizations-get.html)
:   Method: get

    Path: `/api/v2/organizations/`

[List Projects for an Organization](op-api-v2-organizations-id-projects-get.html)
:   Method: get

    Path: `/api/v2/organizations/{id}/projects/`

[List Roles for an Organization](op-api-v2-organizations-id-object_roles-get.html)
:   Method: get

    Path: `/api/v2/organizations/{id}/object_roles/`

[List Teams for an Organization](op-api-v2-organizations-id-teams-get.html)
:   Method: get

    Path: `/api/v2/organizations/{id}/teams/`

[List Users](op-api-v2-organizations-id-access_list-get.html)
:   Method: get

    Path: `/api/v2/organizations/{id}/access_list/`

[List Users for an Organization](op-api-v2-organizations-id-users-get.html)
:   Method: get

    Path: `/api/v2/organizations/{id}/users/`

[List Workflow Job Templates for an Organization](op-api-v2-organizations-id-workflow_job_templates-get.html)
:   Method: get

    Path: `/api/v2/organizations/{id}/workflow_job_templates/`

[Retrieve an Organization](op-api-v2-organizations-id-get.html)
:   Method: get

    Path: `/api/v2/organizations/{id}/`

[Update an Organization](op-api-v2-organizations-id-patch.html)
:   Method: patch

    Path: `/api/v2/organizations/{id}/`

[Update an Organization](op-api-v2-organizations-id-put.html)
:   Method: put

    Path: `/api/v2/organizations/{id}/`

Ping

REST API endpoints for Ping

[Return Some Basic Information About This Instance](op-api-v2-ping-get.html)
:   Method: get

    Path: `/api/v2/ping/`

Project Updates

REST API endpoints for Project Updates

[Cancel Project Update](op-api-v2-project_updates-id-cancel-get.html)
:   Method: get

    Path: `/api/v2/project_updates/{id}/cancel/`

[Cancel Project Update](op-api-v2-project_updates-id-cancel-post.html)
:   Method: post

    Path: `/api/v2/project_updates/{id}/cancel/`

[Delete a Project Update](op-api-v2-project_updates-id-delete.html)
:   Method: delete

    Path: `/api/v2/project_updates/{id}/`

[List Inventory Updates for a Project Update](op-api-v2-project_updates-id-scm_inventory_updates-get.html)
:   Method: get

    Path: `/api/v2/project_updates/{id}/scm_inventory_updates/`

[List Notifications for a Project Update](op-api-v2-project_updates-id-notifications-get.html)
:   Method: get

    Path: `/api/v2/project_updates/{id}/notifications/`

[List Project Update Events for a Project Update](op-api-v2-project_updates-id-events-get.html)
:   Method: get

    Path: `/api/v2/project_updates/{id}/events/`

[List Project Updates](op-api-v2-project_updates-get.html)
:   Method: get

    Path: `/api/v2/project_updates/`

[Retrieve a Project Update](op-api-v2-project_updates-id-get.html)
:   Method: get

    Path: `/api/v2/project_updates/{id}/`

[Retrieve Project Update Stdout](op-api-v2-project_updates-id-stdout-get.html)
:   Method: get

    Path: `/api/v2/project_updates/{id}/stdout/`

Projects

REST API endpoints for Projects

[Create a Notification Template for a Project](op-api-v2-projects-id-notification_templates_error-post.html)
:   Method: post

    Path: `/api/v2/projects/{id}/notification_templates_error/`

[Create a Notification Template for a Project](op-api-v2-projects-id-notification_templates_started-post.html)
:   Method: post

    Path: `/api/v2/projects/{id}/notification_templates_started/`

[Create a Notification Template for a Project](op-api-v2-projects-id-notification_templates_success-post.html)
:   Method: post

    Path: `/api/v2/projects/{id}/notification_templates_success/`

[Create a Project](op-api-v2-projects-post.html)
:   Method: post

    Path: `/api/v2/projects/`

[Create a Schedule for a Project](op-api-v2-projects-id-schedules-post.html)
:   Method: post

    Path: `/api/v2/projects/{id}/schedules/`

[Delete a Project](op-api-v2-projects-id-delete.html)
:   Method: delete

    Path: `/api/v2/projects/{id}/`

[List Activity Streams for a Project](op-api-v2-projects-id-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/projects/{id}/activity_stream/`

[List Inventory Sources for a Project](op-api-v2-projects-id-scm_inventory_sources-get.html)
:   Method: get

    Path: `/api/v2/projects/{id}/scm_inventory_sources/`

[List Notification Templates for a Project](op-api-v2-projects-id-notification_templates_error-get.html)
:   Method: get

    Path: `/api/v2/projects/{id}/notification_templates_error/`

[List Notification Templates for a Project](op-api-v2-projects-id-notification_templates_started-get.html)
:   Method: get

    Path: `/api/v2/projects/{id}/notification_templates_started/`

[List Notification Templates for a Project](op-api-v2-projects-id-notification_templates_success-get.html)
:   Method: get

    Path: `/api/v2/projects/{id}/notification_templates_success/`

[List Project Updates for a Project](op-api-v2-projects-id-project_updates-get.html)
:   Method: get

    Path: `/api/v2/projects/{id}/project_updates/`

[List Projects](op-api-v2-projects-get.html)
:   Method: get

    Path: `/api/v2/projects/`

[List Roles for a Project](op-api-v2-projects-id-object_roles-get.html)
:   Method: get

    Path: `/api/v2/projects/{id}/object_roles/`

[List Schedules for a Project](op-api-v2-projects-id-schedules-get.html)
:   Method: get

    Path: `/api/v2/projects/{id}/schedules/`

[List Teams](op-api-v2-projects-id-teams-get.html)
:   Method: get

    Path: `/api/v2/projects/{id}/teams/`

[List Users](op-api-v2-projects-id-access_list-get.html)
:   Method: get

    Path: `/api/v2/projects/{id}/access_list/`

[Projects Copy Create](op-api-v2-projects-id-copy-post.html)
:   Method: post

    Path: `/api/v2/projects/{id}/copy/`

[Projects Copy List](op-api-v2-projects-id-copy-get.html)
:   Method: get

    Path: `/api/v2/projects/{id}/copy/`

[Retrieve a Project](op-api-v2-projects-id-get.html)
:   Method: get

    Path: `/api/v2/projects/{id}/`

[Retrieve a Project](op-api-v2-projects-id-inventories-get.html)
:   Method: get

    Path: `/api/v2/projects/{id}/inventories/`

[Retrieve Project Playbooks](op-api-v2-projects-id-playbooks-get.html)
:   Method: get

    Path: `/api/v2/projects/{id}/playbooks/`

[Update a Project](op-api-v2-projects-id-patch.html)
:   Method: patch

    Path: `/api/v2/projects/{id}/`

[Update a Project](op-api-v2-projects-id-put.html)
:   Method: put

    Path: `/api/v2/projects/{id}/`

[Update Project](op-api-v2-projects-id-update-get.html)
:   Method: get

    Path: `/api/v2/projects/{id}/update/`

[Update Project](op-api-v2-projects-id-update-post.html)
:   Method: post

    Path: `/api/v2/projects/{id}/update/`

Roles

REST API endpoints for Roles

[Create a Team for a Role](op-api-v2-roles-id-teams-post.html)
:   Method: post

    Path: `/api/v2/roles/{id}/teams/`

[Create a User for a Role](op-api-v2-roles-id-users-post.html)
:   Method: post

    Path: `/api/v2/roles/{id}/users/`

[List Roles](op-api-v2-roles-get.html)
:   Method: get

    Path: `/api/v2/roles/`

[List Roles for a Role](op-api-v2-roles-id-children-get.html)
:   Method: get

    Path: `/api/v2/roles/{id}/children/`

[List Roles for a Role](op-api-v2-roles-id-parents-get.html)
:   Method: get

    Path: `/api/v2/roles/{id}/parents/`

[List Teams for a Role](op-api-v2-roles-id-teams-get.html)
:   Method: get

    Path: `/api/v2/roles/{id}/teams/`

[List Users for a Role](op-api-v2-roles-id-users-get.html)
:   Method: get

    Path: `/api/v2/roles/{id}/users/`

[Retrieve a Role](op-api-v2-roles-id-get.html)
:   Method: get

    Path: `/api/v2/roles/{id}/`

Schedules

REST API endpoints for Schedules

[Create a Credential for a Schedule](op-api-v2-schedules-id-credentials-post.html)
:   Method: post

    Path: `/api/v2/schedules/{id}/credentials/`

[Create a Label for a Schedule](op-api-v2-schedules-id-labels-post.html)
:   Method: post

    Path: `/api/v2/schedules/{id}/labels/`

[Create an Instance Group for a Schedule](op-api-v2-schedules-id-instance_groups-post.html)
:   Method: post

    Path: `/api/v2/schedules/{id}/instance_groups/`

[Delete a Schedule](op-api-v2-schedules-id-delete.html)
:   Method: delete

    Path: `/api/v2/schedules/{id}/`

[List Credentials for a Schedule](op-api-v2-schedules-id-credentials-get.html)
:   Method: get

    Path: `/api/v2/schedules/{id}/credentials/`

[List Instance Groups for a Schedule](op-api-v2-schedules-id-instance_groups-get.html)
:   Method: get

    Path: `/api/v2/schedules/{id}/instance_groups/`

[List Labels for a Schedule](op-api-v2-schedules-id-labels-get.html)
:   Method: get

    Path: `/api/v2/schedules/{id}/labels/`

[List Schedules](op-api-v2-schedules-get.html)
:   Method: get

    Path: `/api/v2/schedules/`

[List Unified Jobs for a Schedule](op-api-v2-schedules-id-jobs-get.html)
:   Method: get

    Path: `/api/v2/schedules/{id}/jobs/`

[Retrieve a Schedule](op-api-v2-schedules-id-get.html)
:   Method: get

    Path: `/api/v2/schedules/{id}/`

[Schedule Details ================ The Following Lists the Expected Format and Details of Our Rrules](op-api-v2-schedules-post.html)
:   Method: post

    Path: `/api/v2/schedules/`

[Schedules Preview Create](op-api-v2-schedules-preview-post.html)
:   Method: post

    Path: `/api/v2/schedules/preview/`

[Schedules Zoneinfo List](op-api-v2-schedules-zoneinfo-get.html)
:   Method: get

    Path: `/api/v2/schedules/zoneinfo/`

[Update a Schedule](op-api-v2-schedules-id-patch.html)
:   Method: patch

    Path: `/api/v2/schedules/{id}/`

[Update a Schedule](op-api-v2-schedules-id-put.html)
:   Method: put

    Path: `/api/v2/schedules/{id}/`

Settings

REST API endpoints for Settings

[Delete a Setting](op-api-v2-settings-category_slug-delete.html)
:   Method: delete

    Path: `/api/v2/settings/{category_slug}/`

[List Settings](op-api-v2-settings-get.html)
:   Method: get

    Path: `/api/v2/settings/`

[Retrieve a Setting](op-api-v2-settings-category_slug-get.html)
:   Method: get

    Path: `/api/v2/settings/{category_slug}/`

[Settings Logging Test Create](op-api-v2-settings-logging-test-post.html)
:   Method: post

    Path: `/api/v2/settings/logging/test/`

[Update a Setting](op-api-v2-settings-category_slug-patch.html)
:   Method: patch

    Path: `/api/v2/settings/{category_slug}/`

[Update a Setting](op-api-v2-settings-category_slug-put.html)
:   Method: put

    Path: `/api/v2/settings/{category_slug}/`

System Job Templates

REST API endpoints for System Job Templates

[Create a Notification Template for a System Job Template](op-api-v2-system_job_templates-id-notification_templates_error-post.html)
:   Method: post

    Path: `/api/v2/system_job_templates/{id}/notification_templates_error/`

[Create a Notification Template for a System Job Template](op-api-v2-system_job_templates-id-notification_templates_started-post.html)
:   Method: post

    Path: `/api/v2/system_job_templates/{id}/notification_templates_started/`

[Create a Notification Template for a System Job Template](op-api-v2-system_job_templates-id-notification_templates_success-post.html)
:   Method: post

    Path: `/api/v2/system_job_templates/{id}/notification_templates_success/`

[Create a Schedule for a System Job Template](op-api-v2-system_job_templates-id-schedules-post.html)
:   Method: post

    Path: `/api/v2/system_job_templates/{id}/schedules/`

[Launch a Job Template](op-api-v2-system_job_templates-id-launch-get.html)
:   Method: get

    Path: `/api/v2/system_job_templates/{id}/launch/`

[Launch a Job Template](op-api-v2-system_job_templates-id-launch-post.html)
:   Method: post

    Path: `/api/v2/system_job_templates/{id}/launch/`

[List Notification Templates for a System Job Template](op-api-v2-system_job_templates-id-notification_templates_error-get.html)
:   Method: get

    Path: `/api/v2/system_job_templates/{id}/notification_templates_error/`

[List Notification Templates for a System Job Template](op-api-v2-system_job_templates-id-notification_templates_started-get.html)
:   Method: get

    Path: `/api/v2/system_job_templates/{id}/notification_templates_started/`

[List Notification Templates for a System Job Template](op-api-v2-system_job_templates-id-notification_templates_success-get.html)
:   Method: get

    Path: `/api/v2/system_job_templates/{id}/notification_templates_success/`

[List Schedules for a System Job Template](op-api-v2-system_job_templates-id-schedules-get.html)
:   Method: get

    Path: `/api/v2/system_job_templates/{id}/schedules/`

[List System Job Templates](op-api-v2-system_job_templates-get.html)
:   Method: get

    Path: `/api/v2/system_job_templates/`

[List System Jobs for a System Job Template](op-api-v2-system_job_templates-id-jobs-get.html)
:   Method: get

    Path: `/api/v2/system_job_templates/{id}/jobs/`

[Retrieve a System Job Template](op-api-v2-system_job_templates-id-get.html)
:   Method: get

    Path: `/api/v2/system_job_templates/{id}/`

System Jobs

REST API endpoints for System Jobs

[Delete a System Job](op-api-v2-system_jobs-id-delete.html)
:   Method: delete

    Path: `/api/v2/system_jobs/{id}/`

[List Notifications for a System Job](op-api-v2-system_jobs-id-notifications-get.html)
:   Method: get

    Path: `/api/v2/system_jobs/{id}/notifications/`

[List System Job Events for a System Job](op-api-v2-system_jobs-id-events-get.html)
:   Method: get

    Path: `/api/v2/system_jobs/{id}/events/`

[List System Jobs](op-api-v2-system_jobs-get.html)
:   Method: get

    Path: `/api/v2/system_jobs/`

[Retrieve a System Job](op-api-v2-system_jobs-id-get.html)
:   Method: get

    Path: `/api/v2/system_jobs/{id}/`

[Retrieve a System Job](op-api-v2-system_jobs-id-cancel-get.html)
:   Method: get

    Path: `/api/v2/system_jobs/{id}/cancel/`

[Retrieve a System Job](op-api-v2-system_jobs-id-cancel-post.html)
:   Method: post

    Path: `/api/v2/system_jobs/{id}/cancel/`

Task Manager

REST API endpoints for Task Manager

[Debug Task Manager List](op-api-debug-task_manager-get.html)
:   Method: get

    Path: `/api/debug/task_manager/`

Teams

REST API endpoints for Teams

[Associate Roles With This Team](op-api-v2-teams-id-roles-post.html)
:   Method: post

    Path: `/api/v2/teams/{id}/roles/`

[Create a Credential for a Team](op-api-v2-teams-id-credentials-post.html)
:   Method: post

    Path: `/api/v2/teams/{id}/credentials/`

[Create a Team](op-api-v2-teams-post.html)
:   Method: post

    Path: `/api/v2/teams/`

[Create a User for a Team](op-api-v2-teams-id-users-post.html)
:   Method: post

    Path: `/api/v2/teams/{id}/users/`

[Delete a Team](op-api-v2-teams-id-delete.html)
:   Method: delete

    Path: `/api/v2/teams/{id}/`

[List Activity Streams for a Team](op-api-v2-teams-id-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/teams/{id}/activity_stream/`

[List Credentials for a Team](op-api-v2-teams-id-credentials-get.html)
:   Method: get

    Path: `/api/v2/teams/{id}/credentials/`

[List Projects for a Team](op-api-v2-teams-id-projects-get.html)
:   Method: get

    Path: `/api/v2/teams/{id}/projects/`

[List Roles for a Team](op-api-v2-teams-id-object_roles-get.html)
:   Method: get

    Path: `/api/v2/teams/{id}/object_roles/`

[List Roles for a Team](op-api-v2-teams-id-roles-get.html)
:   Method: get

    Path: `/api/v2/teams/{id}/roles/`

[List Teams](op-api-v2-teams-get.html)
:   Method: get

    Path: `/api/v2/teams/`

[List Users](op-api-v2-teams-id-access_list-get.html)
:   Method: get

    Path: `/api/v2/teams/{id}/access_list/`

[List Users for a Team](op-api-v2-teams-id-users-get.html)
:   Method: get

    Path: `/api/v2/teams/{id}/users/`

[Retrieve a Team](op-api-v2-teams-id-get.html)
:   Method: get

    Path: `/api/v2/teams/{id}/`

[Update a Team](op-api-v2-teams-id-patch.html)
:   Method: patch

    Path: `/api/v2/teams/{id}/`

[Update a Team](op-api-v2-teams-id-put.html)
:   Method: put

    Path: `/api/v2/teams/{id}/`

Tokens

REST API endpoints for Tokens

[Create an Access Token](op-api-v2-tokens-post.html)
:   Method: post

    Path: `/api/v2/tokens/`

[Delete an Access Token](op-api-v2-tokens-id-delete.html)
:   Method: delete

    Path: `/api/v2/tokens/{id}/`

[List Access Tokens](op-api-v2-tokens-get.html)
:   Method: get

    Path: `/api/v2/tokens/`

[List Activity Streams for an Access Token](op-api-v2-tokens-id-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/tokens/{id}/activity_stream/`

[Retrieve an Access Token](op-api-v2-tokens-id-get.html)
:   Method: get

    Path: `/api/v2/tokens/{id}/`

[Update an Access Token](op-api-v2-tokens-id-patch.html)
:   Method: patch

    Path: `/api/v2/tokens/{id}/`

[Update an Access Token](op-api-v2-tokens-id-put.html)
:   Method: put

    Path: `/api/v2/tokens/{id}/`

Unified Job Templates

REST API endpoints for Unified Job Templates

[List Unified Job Templates](op-api-v2-unified_job_templates-get.html)
:   Method: get

    Path: `/api/v2/unified_job_templates/`

Unified Jobs

REST API endpoints for Unified Jobs

[List Unified Jobs](op-api-v2-unified_jobs-get.html)
:   Method: get

    Path: `/api/v2/unified_jobs/`

Users

REST API endpoints for Users

[Associate Roles With This User](op-api-v2-users-id-roles-post.html)
:   Method: post

    Path: `/api/v2/users/{id}/roles/`

[Create a Credential for a User](op-api-v2-users-id-credentials-post.html)
:   Method: post

    Path: `/api/v2/users/{id}/credentials/`

[Create a User](op-api-v2-users-post.html)
:   Method: post

    Path: `/api/v2/users/`

[Create an Access Token for a User](op-api-v2-users-id-authorized_tokens-post.html)
:   Method: post

    Path: `/api/v2/users/{id}/authorized_tokens/`

[Create an Access Token for a User](op-api-v2-users-id-personal_tokens-post.html)
:   Method: post

    Path: `/api/v2/users/{id}/personal_tokens/`

[Create an Access Token for a User](op-api-v2-users-id-tokens-post.html)
:   Method: post

    Path: `/api/v2/users/{id}/tokens/`

[Create an Application](op-api-v2-users-id-applications-post.html)
:   Method: post

    Path: `/api/v2/users/{id}/applications/`

[Delete a User](op-api-v2-users-id-delete.html)
:   Method: delete

    Path: `/api/v2/users/{id}/`

[List Access Tokens for a User](op-api-v2-users-id-authorized_tokens-get.html)
:   Method: get

    Path: `/api/v2/users/{id}/authorized_tokens/`

[List Access Tokens for a User](op-api-v2-users-id-personal_tokens-get.html)
:   Method: get

    Path: `/api/v2/users/{id}/personal_tokens/`

[List Access Tokens for a User](op-api-v2-users-id-tokens-get.html)
:   Method: get

    Path: `/api/v2/users/{id}/tokens/`

[List Activity Streams for a User](op-api-v2-users-id-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/users/{id}/activity_stream/`

[List Applications](op-api-v2-users-id-applications-get.html)
:   Method: get

    Path: `/api/v2/users/{id}/applications/`

[List Credentials for a User](op-api-v2-users-id-credentials-get.html)
:   Method: get

    Path: `/api/v2/users/{id}/credentials/`

[List Organizations Administered by This User](op-api-v2-users-id-admin_of_organizations-get.html)
:   Method: get

    Path: `/api/v2/users/{id}/admin_of_organizations/`

[List Organizations for a User](op-api-v2-users-id-organizations-get.html)
:   Method: get

    Path: `/api/v2/users/{id}/organizations/`

[List Projects for a User](op-api-v2-users-id-projects-get.html)
:   Method: get

    Path: `/api/v2/users/{id}/projects/`

[List Roles for a User](op-api-v2-users-id-roles-get.html)
:   Method: get

    Path: `/api/v2/users/{id}/roles/`

[List Teams for a User](op-api-v2-users-id-teams-get.html)
:   Method: get

    Path: `/api/v2/users/{id}/teams/`

[List Users](op-api-v2-users-get.html)
:   Method: get

    Path: `/api/v2/users/`

[List Users](op-api-v2-users-id-access_list-get.html)
:   Method: get

    Path: `/api/v2/users/{id}/access_list/`

[Retrieve a User](op-api-v2-users-id-get.html)
:   Method: get

    Path: `/api/v2/users/{id}/`

[Update a User](op-api-v2-users-id-patch.html)
:   Method: patch

    Path: `/api/v2/users/{id}/`

[Update a User](op-api-v2-users-id-put.html)
:   Method: put

    Path: `/api/v2/users/{id}/`

Workflow Approval Templates

REST API endpoints for Workflow Approval Templates

[Delete a Workflow Approval Template](op-api-v2-workflow_approval_templates-id-delete.html)
:   Method: delete

    Path: `/api/v2/workflow_approval_templates/{id}/`

[List Workflow Approvals for a Workflow Approval Template](op-api-v2-workflow_approval_templates-id-approvals-get.html)
:   Method: get

    Path: `/api/v2/workflow_approval_templates/{id}/approvals/`

[Retrieve a Workflow Approval Template](op-api-v2-workflow_approval_templates-id-get.html)
:   Method: get

    Path: `/api/v2/workflow_approval_templates/{id}/`

[Update a Workflow Approval Template](op-api-v2-workflow_approval_templates-id-patch.html)
:   Method: patch

    Path: `/api/v2/workflow_approval_templates/{id}/`

[Update a Workflow Approval Template](op-api-v2-workflow_approval_templates-id-put.html)
:   Method: put

    Path: `/api/v2/workflow_approval_templates/{id}/`

Workflow Approvals

REST API endpoints for Workflow Approvals

[Delete a Workflow Approval](op-api-v2-workflow_approvals-id-delete.html)
:   Method: delete

    Path: `/api/v2/workflow_approvals/{id}/`

[List Workflow Approvals](op-api-v2-workflow_approvals-get.html)
:   Method: get

    Path: `/api/v2/workflow_approvals/`

[Retrieve a Workflow Approval](op-api-v2-workflow_approvals-id-get.html)
:   Method: get

    Path: `/api/v2/workflow_approvals/{id}/`

[Retrieve a Workflow Approval](op-api-v2-workflow_approvals-id-approve-get.html)
:   Method: get

    Path: `/api/v2/workflow_approvals/{id}/approve/`

[Retrieve a Workflow Approval](op-api-v2-workflow_approvals-id-approve-post.html)
:   Method: post

    Path: `/api/v2/workflow_approvals/{id}/approve/`

[Retrieve a Workflow Approval](op-api-v2-workflow_approvals-id-deny-get.html)
:   Method: get

    Path: `/api/v2/workflow_approvals/{id}/deny/`

[Retrieve a Workflow Approval](op-api-v2-workflow_approvals-id-deny-post.html)
:   Method: post

    Path: `/api/v2/workflow_approvals/{id}/deny/`

Workflow Job Nodes

REST API endpoints for Workflow Job Nodes

[Create an Instance Group for a Workflow Job Node](op-api-v2-workflow_job_nodes-id-instance_groups-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_nodes/{id}/instance_groups/`

[List Credentials for a Workflow Job Node](op-api-v2-workflow_job_nodes-id-credentials-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_nodes/{id}/credentials/`

[List Instance Groups for a Workflow Job Node](op-api-v2-workflow_job_nodes-id-instance_groups-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_nodes/{id}/instance_groups/`

[List Labels for a Workflow Job Node](op-api-v2-workflow_job_nodes-id-labels-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_nodes/{id}/labels/`

[List Workflow Job Nodes](op-api-v2-workflow_job_nodes-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_nodes/`

[List Workflow Job Nodes for a Workflow Job Node](op-api-v2-workflow_job_nodes-id-always_nodes-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_nodes/{id}/always_nodes/`

[List Workflow Job Nodes for a Workflow Job Node](op-api-v2-workflow_job_nodes-id-failure_nodes-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_nodes/{id}/failure_nodes/`

[List Workflow Job Nodes for a Workflow Job Node](op-api-v2-workflow_job_nodes-id-success_nodes-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_nodes/{id}/success_nodes/`

[Retrieve a Workflow Job Node](op-api-v2-workflow_job_nodes-id-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_nodes/{id}/`

Workflow Job Template Nodes

REST API endpoints for Workflow Job Template Nodes

[Create a Credential for a Workflow Job Template Node](op-api-v2-workflow_job_template_nodes-id-credentials-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_template_nodes/{id}/credentials/`

[Create a Label for a Workflow Job Template Node](op-api-v2-workflow_job_template_nodes-id-labels-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_template_nodes/{id}/labels/`

[Create a Workflow Job Template Node](op-api-v2-workflow_job_template_nodes-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_template_nodes/`

[Create a Workflow Job Template Node for a Workflow Job Template Node](op-api-v2-workflow_job_template_nodes-id-always_nodes-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_template_nodes/{id}/always_nodes/`

[Create a Workflow Job Template Node for a Workflow Job Template Node](op-api-v2-workflow_job_template_nodes-id-failure_nodes-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_template_nodes/{id}/failure_nodes/`

[Create a Workflow Job Template Node for a Workflow Job Template Node](op-api-v2-workflow_job_template_nodes-id-success_nodes-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_template_nodes/{id}/success_nodes/`

[Create an Instance Group for a Workflow Job Template Node](op-api-v2-workflow_job_template_nodes-id-instance_groups-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_template_nodes/{id}/instance_groups/`

[Delete a Workflow Job Template Node](op-api-v2-workflow_job_template_nodes-id-delete.html)
:   Method: delete

    Path: `/api/v2/workflow_job_template_nodes/{id}/`

[List Credentials for a Workflow Job Template Node](op-api-v2-workflow_job_template_nodes-id-credentials-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_template_nodes/{id}/credentials/`

[List Instance Groups for a Workflow Job Template Node](op-api-v2-workflow_job_template_nodes-id-instance_groups-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_template_nodes/{id}/instance_groups/`

[List Labels for a Workflow Job Template Node](op-api-v2-workflow_job_template_nodes-id-labels-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_template_nodes/{id}/labels/`

[List Workflow Job Template Nodes](op-api-v2-workflow_job_template_nodes-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_template_nodes/`

[List Workflow Job Template Nodes for a Workflow Job Template Node](op-api-v2-workflow_job_template_nodes-id-always_nodes-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_template_nodes/{id}/always_nodes/`

[List Workflow Job Template Nodes for a Workflow Job Template Node](op-api-v2-workflow_job_template_nodes-id-failure_nodes-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_template_nodes/{id}/failure_nodes/`

[List Workflow Job Template Nodes for a Workflow Job Template Node](op-api-v2-workflow_job_template_nodes-id-success_nodes-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_template_nodes/{id}/success_nodes/`

[Retrieve a Workflow Job Template Node](op-api-v2-workflow_job_template_nodes-id-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_template_nodes/{id}/`

[Retrieve a Workflow Job Template Node](op-api-v2-workflow_job_template_nodes-id-create_approval_template-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_template_nodes/{id}/create_approval_template/`

[Retrieve a Workflow Job Template Node](op-api-v2-workflow_job_template_nodes-id-create_approval_template-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_template_nodes/{id}/create_approval_template/`

[Update a Workflow Job Template Node](op-api-v2-workflow_job_template_nodes-id-patch.html)
:   Method: patch

    Path: `/api/v2/workflow_job_template_nodes/{id}/`

[Update a Workflow Job Template Node](op-api-v2-workflow_job_template_nodes-id-put.html)
:   Method: put

    Path: `/api/v2/workflow_job_template_nodes/{id}/`

Workflow Job Templates

REST API endpoints for Workflow Job Templates

[Copy a Workflow Job Template](op-api-v2-workflow_job_templates-id-copy-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_templates/{id}/copy/`

[Copy a Workflow Job Template](op-api-v2-workflow_job_templates-id-copy-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_templates/{id}/copy/`

[Create a Label for a Workflow Job Template](op-api-v2-workflow_job_templates-id-labels-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_templates/{id}/labels/`

[Create a Notification Template for a Workflow Job Template](op-api-v2-workflow_job_templates-id-notification_templates_approvals-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_templates/{id}/notification_templates_approvals/`

[Create a Notification Template for a Workflow Job Template](op-api-v2-workflow_job_templates-id-notification_templates_error-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_templates/{id}/notification_templates_error/`

[Create a Notification Template for a Workflow Job Template](op-api-v2-workflow_job_templates-id-notification_templates_started-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_templates/{id}/notification_templates_started/`

[Create a Notification Template for a Workflow Job Template](op-api-v2-workflow_job_templates-id-notification_templates_success-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_templates/{id}/notification_templates_success/`

[Create a Schedule for a Workflow Job Template](op-api-v2-workflow_job_templates-id-schedules-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_templates/{id}/schedules/`

[Create a Workflow Job Template](op-api-v2-workflow_job_templates-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_templates/`

[Delete a Workflow Job Template](op-api-v2-workflow_job_templates-id-delete.html)
:   Method: delete

    Path: `/api/v2/workflow_job_templates/{id}/`

[Launch a Workflow Job Template](op-api-v2-workflow_job_templates-id-launch-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_templates/{id}/launch/`

[Launch a Workflow Job Template](op-api-v2-workflow_job_templates-id-launch-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_templates/{id}/launch/`

[List Activity Streams for a Workflow Job Template](op-api-v2-workflow_job_templates-id-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_templates/{id}/activity_stream/`

[List Labels for a Workflow Job Template](op-api-v2-workflow_job_templates-id-labels-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_templates/{id}/labels/`

[List Notification Templates for a Workflow Job Template](op-api-v2-workflow_job_templates-id-notification_templates_approvals-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_templates/{id}/notification_templates_approvals/`

[List Notification Templates for a Workflow Job Template](op-api-v2-workflow_job_templates-id-notification_templates_error-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_templates/{id}/notification_templates_error/`

[List Notification Templates for a Workflow Job Template](op-api-v2-workflow_job_templates-id-notification_templates_started-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_templates/{id}/notification_templates_started/`

[List Notification Templates for a Workflow Job Template](op-api-v2-workflow_job_templates-id-notification_templates_success-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_templates/{id}/notification_templates_success/`

[List Roles for a Workflow Job Template](op-api-v2-workflow_job_templates-id-object_roles-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_templates/{id}/object_roles/`

[List Schedules for a Workflow Job Template](op-api-v2-workflow_job_templates-id-schedules-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_templates/{id}/schedules/`

[List Users](op-api-v2-workflow_job_templates-id-access_list-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_templates/{id}/access_list/`

[List Workflow Job Templates](op-api-v2-workflow_job_templates-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_templates/`

[List Workflow Jobs for a Workflow Job Template](op-api-v2-workflow_job_templates-id-workflow_jobs-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_templates/{id}/workflow_jobs/`

[POST Requests to This Resource Should Include the Full Specification for a Workflow Job Template's Survey](op-api-v2-workflow_job_templates-id-survey_spec-delete.html)
:   Method: delete

    Path: `/api/v2/workflow_job_templates/{id}/survey_spec/`

[POST Requests to This Resource Should Include the Full Specification for a Workflow Job Template's Survey](op-api-v2-workflow_job_templates-id-survey_spec-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_templates/{id}/survey_spec/`

[POST Requests to This Resource Should Include the Full Specification for a Workflow Job Template's Survey](op-api-v2-workflow_job_templates-id-survey_spec-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_templates/{id}/survey_spec/`

[Retrieve a Workflow Job Template](op-api-v2-workflow_job_templates-id-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_templates/{id}/`

[Update a Workflow Job Template](op-api-v2-workflow_job_templates-id-patch.html)
:   Method: patch

    Path: `/api/v2/workflow_job_templates/{id}/`

[Update a Workflow Job Template](op-api-v2-workflow_job_templates-id-put.html)
:   Method: put

    Path: `/api/v2/workflow_job_templates/{id}/`

[Workflow Job Template Workflow Node List](op-api-v2-workflow_job_templates-id-workflow_nodes-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_templates/{id}/workflow_nodes/`

[Workflow Job Template Workflow Node List](op-api-v2-workflow_job_templates-id-workflow_nodes-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_templates/{id}/workflow_nodes/`

[Workflow Job Templates Bitbucket Dc Create](op-api-v2-workflow_job_templates-id-bitbucket_dc-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_templates/{id}/bitbucket_dc/`

[Workflow Job Templates Github Create](op-api-v2-workflow_job_templates-id-github-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_templates/{id}/github/`

[Workflow Job Templates Gitlab Create](op-api-v2-workflow_job_templates-id-gitlab-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_templates/{id}/gitlab/`

[Workflow Job Templates Webhook Key Create](op-api-v2-workflow_job_templates-id-webhook_key-post.html)
:   Method: post

    Path: `/api/v2/workflow_job_templates/{id}/webhook_key/`

[Workflow Job Templates Webhook Key List](op-api-v2-workflow_job_templates-id-webhook_key-get.html)
:   Method: get

    Path: `/api/v2/workflow_job_templates/{id}/webhook_key/`

Workflow Jobs

REST API endpoints for Workflow Jobs

[Cancel Workflow Job](op-api-v2-workflow_jobs-id-cancel-get.html)
:   Method: get

    Path: `/api/v2/workflow_jobs/{id}/cancel/`

[Cancel Workflow Job](op-api-v2-workflow_jobs-id-cancel-post.html)
:   Method: post

    Path: `/api/v2/workflow_jobs/{id}/cancel/`

[Delete a Workflow Job](op-api-v2-workflow_jobs-id-delete.html)
:   Method: delete

    Path: `/api/v2/workflow_jobs/{id}/`

[List Activity Streams for a Workflow Job](op-api-v2-workflow_jobs-id-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/workflow_jobs/{id}/activity_stream/`

[List Labels for a Workflow Job](op-api-v2-workflow_jobs-id-labels-get.html)
:   Method: get

    Path: `/api/v2/workflow_jobs/{id}/labels/`

[List Notifications for a Workflow Job](op-api-v2-workflow_jobs-id-notifications-get.html)
:   Method: get

    Path: `/api/v2/workflow_jobs/{id}/notifications/`

[List Workflow Job Nodes for a Workflow Job](op-api-v2-workflow_jobs-id-workflow_nodes-get.html)
:   Method: get

    Path: `/api/v2/workflow_jobs/{id}/workflow_nodes/`

[List Workflow Jobs](op-api-v2-workflow_jobs-get.html)
:   Method: get

    Path: `/api/v2/workflow_jobs/`

[Relaunch a Workflow Job](op-api-v2-workflow_jobs-id-relaunch-get.html)
:   Method: get

    Path: `/api/v2/workflow_jobs/{id}/relaunch/`

[Relaunch a Workflow Job](op-api-v2-workflow_jobs-id-relaunch-post.html)
:   Method: post

    Path: `/api/v2/workflow_jobs/{id}/relaunch/`

[Retrieve a Workflow Job](op-api-v2-workflow_jobs-id-get.html)
:   Method: get

    Path: `/api/v2/workflow_jobs/{id}/`

Workflow Manager

REST API endpoints for Workflow Manager

[Debug Workflow Manager List](op-api-debug-workflow_manager-get.html)
:   Method: get

    Path: `/api/debug/workflow_manager/`


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/intro.html -->

## Introduction

This document describes the Oracle Linux Automation Manager 2.3 REST API and the
Command-Line Interface.

The REST API and the Command-Line Interface is based on the AWX version 23.7.0 open
source software REST API and Command-Line Interface and includes all AWX version 23.7.0
functionality. However, the functionality supported by Oracle Linux Automation Manager
is limited to those features described in the [Oracle Linux Automation Manager](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/) documentation.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/quick-start.html -->

## REST API Quick Start

Set up your environment and use the Oracle Linux Automation Manager REST API to manager
your Oracle Linux Automation Manager server.

Prerequisites

|  |  |
| --- | --- |
| Prerequisite | More Information |
| Install and start Oracle Linux Automation Manager. | See the [Oracle Linux Automation Manager Installation Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install2.3/) |
| Install cURL. | [Installing and Using cURL](use-curl.html "The examples within this document use cURL to show how to access and use the Oracle Linux Automation Manager REST API.") |
| Set up authentication. | [Authenticating](authenticate.html) |
| Access the REST API. | [Accessing the REST API](accessing_api.html "You can access REST API provided resources (data entities) using URI paths.") |
| Send requests. | [Sending Requests](send-requests.html) |
| Order and sort requests. | [Ordering and Sorting](sort.html) |
| Search text fields texts. | [Searching Text Fields](searching.html) |
| Filter results using operators. | [Filtering Results Using Operators](filtering.html) |
| Use pagination to limite response length. | [Limiting Response Results Using Pagination](pagination.html) |
| Access resources using named URLs. | [Accessing Resources Using Named URLs](configuration_settings.html) |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/use-curl.html -->

## Installing and Using cURL

The examples within this document use cURL to show how to access and use the Oracle
Linux Automation Manager REST API.

Task 1: Install cURL

To connect securely to the server, you must install a version of cURL that provide an
SSL certificate authority (CA) certificate file or bundle to authenticate against a
CA certificate. For more information about CA Certificate authentication, see [Authenticating](authenticate.html).

The following procedure show how to install cURL on an Oracle Linux 8 or 9
system.

1. Verify whether cURL is already installed on the system.

   `sudo dnf info curl`

   If the package is installed, you see it in the Installed Packages
   List. If you don't have it installed, you see it listed in the Available
   Packages list. If cURL isn't available in any repo, enable the
   ol8\_baseos\_latest or ol9\_baseos\_latest repo and repeat
   this step.
2. Install cURL if not already installed.

   `sudo dnf install curl`

You're now ready to send requests using cURL.

Task 2: Invoke cURL

Invoke cURL and specify one or more of the command line options defined in the
following table, as required, to direct its execution.

| cURL Option | Description |
| --- | --- |
| `-i --include` | Returns the header in the response. |
| `-H --header` | H --header: includes the header in the request. |
| `"Authorization: Bearer <token>"` | Specifies the Oauth2 token required to run the command. |
| `-X <method>` | Indicates the method of request (for example, GET, POST) followed by the API entity path. |
| `-d, --data @file.json` | Identifies the file that contains the request body, in JSON format, on the local machine. Or, you can pass the request body with `-d"{id=5,status='OK'}`. |
| `-F, --form @file.json` | Identifies form data, in JSON format, on the local machine. |
| `-k` | Indicates that a CA authority hasn't been set and the connection is insecure. This option isn't recommended. |

The syntax for cURL commands is as follows:

```
curl -i -H Authorization: Bearer <token>  -X <method> https://<hostname or IP address>/api/v2/<resource-path>
```

In the previous example, <token> is the Oauth2 token generated for the user
account, <method> is action, such as Get, Post, Delete, Put, Patch, and so on,
<hostname or IP address> is the hostname or IP address of the Oracle Linux
Automation Manager server, and <resource-path> is the resource path, such as
users/ or credential\_types/.

For example:

```
curl -i -H "Authorization: Bearer pVQoc51Apt4LNrXrNzoSbaMCDzjK8B" -X GET https://192.102.118.107/api/v2/users/ 
HTTP/1.1 200 OK
Server: nginx/1.20.1
Date: Tue, 24 Jun 2025 13:18:08 GMT
Content-Type: application/json
Content-Length: 1952
Connection: keep-alive
Vary: Accept, Accept-Language, Origin
Allow: GET, POST, HEAD, OPTIONS
X-API-Product-Version: 24.6.1
X-API-Product-Name: AWX
X-API-Node: 100.102.118.107
X-API-Time: 0.024s
Content-Language: en
X-API-Total-Time: 0.059s
X-API-Request-Id: af9121bf2bb748d08c60696334d4ea72
Access-Control-Expose-Headers: X-API-Request-Id
Strict-Transport-Security: max-age=15768000

{"count":2,"next":null,"previous":null,"results":[{"id":1,"type":"user","url":"/api/v2/users/1/","related":{"teams":"/api/v2/users/1/teams/","organizations":"/api/v2/users/1/organizations/","admin_of_organizations":"/api/v2/users/1/admin_of_organizations/","projects":"/api/v2/users/1/projects/","credentials":"/api/v2/users/1/credentials/","roles":"/api/v2/users/1/roles/","activity_stream":"/api/v2/users/1/activity_stream/","access_list":"/api/v2/users/1/access_list/","tokens":"/api/v2/users/1/tokens/","authorized_tokens":"/api/v2/users/1/authorized_tokens/","personal_tokens":"/api/v2/users/1/personal_tokens/"},"summary_fields":{"user_capabilities":{"edit":false,"delete":false}},"created":"2024-08-12T16:46:26.217924Z","modified":"2024-08-12T16:48:34.750654Z","username":"admin","first_name":"","last_name":"","email":"admin@example.com","is_superuser":true,"is_system_auditor":false,"password":"$encrypted$","ldap_dn":"","last_login":"2024-08-12T16:48:34.750654Z","external_account":null,"auth":[]},{"id":2,"type":"user","url":"/api/v2/users/2/","related":{"teams":"/api/v2/users/2/teams/","organizations":"/api/v2/users/2/organizations/","admin_of_organizations":"/api/v2/users/2/admin_of_organizations/","projects":"/api/v2/users/2/projects/","credentials":"/api/v2/users/2/credentials/","roles":"/api/v2/users/2/roles/","activity_stream":"/api/v2/users/2/activity_stream/","access_list":"/api/v2/users/2/access_list/","tokens":"/api/v2/users/2/tokens/","authorized_tokens":"/api/v2/users/2/authorized_tokens/","personal_tokens":"/api/v2/users/2/personal_tokens/"},"summary_fields":{"user_capabilities":{"edit":true,"delete":false}},"created":"2024-08-12T16:49:57.582764Z","modified":null,"username":"automationuser","first_name":"automationuser","last_name":"Automation","email":"automation@account.com","is_superuser":false,"is_system_auditor":true,"password":"$encrypted$","ldap_dn":"","last_login":null,"external_account":null,"auth":[]}]}
```


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/authenticate.html -->

## Authenticating

Oracle Linux Automation Manager uses a certificate authority (CA) certificate with NGINX
and Oauth2 for token based authentication to enable clients to connect securely to the
server. Tokens are easily revoked and are best suited to third-party tooling
integration.

Note:

The Oracle Linux Automation Manager Installation Guide document provides
instructions for setting up the server with a self-signed certificate, however, we
recommend that you use a signed certificate to ensure the server is secure. If you
use the self-signed certificate, then append `-k` to all Oracle Linux
Automation Manager REST API curl or CLI requests to indicate that the request is
insecure.

To setup an Oauth2 token for a user, do the following:

1. Open a terminal on the Oracle Linux Automation Manager server.
2. Run the following commands:

   ```
   sudo su -l awx -s /bin/bash
   awx-manage create_oauth2_token --user=<username>
   ```

   In the previous example,
   <username> is the user name of the account for which you want to create a token.
3. The command generates a token that you must note down in a secure way so that you
   can use it when running cURL or CLI commands. For example, the following token is
   generated using the create\_oauth2\_token command:

   ```
   JWjb1AyOJOWi4yPBYWC7NQofdNSjAM
   ```

To revoke all Oauth2 token for a user, do the following:

1. Open a terminal on the Oracle Linux Automation Manager server.
2. Run the following commands:

   ```
   sudo su -l awx -s /bin/bash
   awx-manage revoke_oauth2_tokens --user=<username>
   ```

   In the previous example,
   <username> is the user name of the account for which you want to revoke all
   tokens. The command lists all revoked tokens for the user. For example, the
   following tokens are revoked when using the revoke\_token2\_tokens command:

   ```
   revoked OAuth2AccessToken aeOy7IWqlt19Kc8Fu1IElsj2w6rCOz
   revoked OAuth2AccessToken JWjb1AyOJOWi4yPBYWC7NQofdNSjAM
   ```


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/accessing_api.html -->

## Accessing the REST API

You can access REST API provided resources (data entities) using URI paths.

Logging in to the REST API

To log in to the Oracle Linux Automation Manager REST API, do the following:

1. Log in to your Oracle Linux Automation Manager server with a user account.

   ```
    https://<hostname or IP address>/api/login/
   ```

   Note:

   In the previous example, <hostname or ip address>
   is the hostname or IP address of the system running Oracle Linux Automation
   Manager . If hostname is used, the host must be resolvable.

   The root
   page for the Oracle Linux Automation Manager REST API appears showing the
   response to a get request at the /api level.
2. In the response area, click one of the /api/v2 links. This performs a get
   request that lists all available resources.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/send-requests.html -->

## Sending Requests

Use these guidelines when sending requests using the Oracle Linux Automation Manager REST
API.

URL Structure

Here's the URL structure for the requests:

```
https://<subdomain>.<domain>.com:<port>/<resource-path>
```

Where:

- `<subdomain.domain>.com:<port>`: Host and port where Oracle Linux Automation
  Manager is running.
- `<resource-path>`: Relative path that defines the
  resource.

Supported Methods

You can perform basic CRUD operations (create, read, update, and delete) on a
resource by using standard HTTP method requests, as summarized in the following
table.

|  |  |
| --- | --- |
| HTTP Method | Description |
| `GET` | Retrieve information about Oracle Linux Automation Manager resources. |
| `HEAD` | Retrieve header information about Oracle Linux Automation Manager resources. |
| `POST` | Create a new Oracle Linux Automation Manager resource. |
| `PUT` | Update resources of the Oracle Linux Automation Manager. |
| `PATCH` | Patch various resources in the Oracle Linux Automation Manager. |
| `DELETE` | Delete the Oracle Linux Automation Manager. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/sort.html -->

## Ordering and Sorting

The following URL is an example query that lists all users available on an Oracle Linux
Automation Manager server:

```
http://<hostname or IP address>/api/v2/users/
```

In the previous example, <hostname or IP address> is the IP address of your Oracle
Linux Automation Manager.

To specify that entities that return more than one result set are returned in a
particular order, you can use GET requests with the order\_by parameter. For example,

```
http://hostname or IP address/api/v2/<multi_result_entity>/order_by=<order_field>
```

In the previous example, <multi\_result\_entity> is an entity that includes more than
one result set, such as, for example, where there are more than one user instance for
the users entity. <order\_field> is the name of the field to order the results by.

You can use the prefix the field name with a dash (-) to sort in reverse. For example,

```
http://hostname or IP address/api/v2/<multi_result_entity>/order_by=-<order_field>
```

Specify multiple sorting fields using a comma (,) to separating each field names. For
example,

```
http://hostname or IP address/api/v2/<multi_result_entity>/order_by=<order_field>,<other_order_field>
```

In the previous example, <other\_order\_field> is another field to include when sorting
results.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/searching.html -->

## Searching Text Fields

You can search for specific text within all designated text fields of a model. For
example,

```
http://<hostname or IP address>/api/v2/<multi_result_entity>/?search=<text>
```

In the previous example, <hostname or IP address> is the IP address of your Oracle
Linux Automation Manager and <text> is the text you want to search.

You can also search across related fields:

```
http://<hostname or IP address>/api/v2/<multi_result_entity>/?related__search=<text>
```


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/filtering.html -->

## Filtering Results Using Operators

You can filter a collection using various operators. For example, to find the users that
contain a specific text:

```
http://<hostname or IP address>/api/v2/<multi_result_entity>/?<field_name>__contains=<text>
```

In the previous example, <hostname or IP address> is the IP address of your Oracle
Linux Automation Manager. <multi\_result\_entity> is an entity that includes more than
one result set, such as, for example, where there are more than one user instance for
the users entity. <field\_name> is the name of the field to apply the search text to,
and <text> is the name of the text to search.

To find a specific match, you can use the following syntax:

```
http://<hostname or IP address>/api/v2/<multi_result_entity>/?<field_name>=<text>
```

For integer type rsources, add \\_\\_int to the end to send the string input value as an
integer. For example,

```
http://<hostname or IP address>/api/v2/<multi_result_entity>/?<field_name>__int=<integer>
```

You can also filter for related resources. For example,

```
http://<hostname or IP address>/api/v2/<multi_result_entity>/?<field_name>__icontains=<text>
```

All resources with a field that includes the text are returned.

You can also filter with multiple fields. For example,

```
http://<hostname or IP address>/api/v2/<multi_result_entity>/?<field_name>__icontains=<text>&<field_name>=<text>
```

For more about available operators types, see the following Web site: <https://docs.djangoproject.com/en/dev/ref/models/querysets/>

You can use additional query string parameters to filter the list of results returned to
those matching a given value. Only fields and relations that exist in the database may
be used for filtering. Any special characters in the specified value should be
url-encoded. For example:

```
?field=value%20xyz
```

Fields may also span relations, only for fields and relationships defined in the
database:

```
?other__field=value
```

To exclude results matching certain criteria, prefix the field parameter with not\_\_:

```
?not__field=value
```

By default, all query string filters are joined using the AND operator, so only the
results matching all filters are returned. To combine results matching any one of
multiple criteria, prefix each query string parameter with or\_\_:

```
?or__field=value&or__field=othervalue
?or__not__field=value&or__field=othervalue
```

The default AND filtering applies all filters simultaneously to each related object being
filtered across database relationships. The chain filter instead applies filters
separately for each related object. To use, prefix the query string parameter with
chain\_\_:

```
?chain__related__field=value&chain__related__field2=othervalue
?chain__not__related__field=value&chain__related__field2=othervalue
```

If the first query above were written as
?related\_\_field=value&related\_\_field2=othervalue, it would return only the primary
objects where the same related object satisfied both conditions. As written using the
chain filter, it would return the intersection of primary objects matching each
condition.

Field lookups may also be used for more advanced queries, by appending the lookup to the
field name:

```
?field__lookup=value
```

The following field lookups are supported:

- exact: Exact match (default lookup if not specified).
- iexact: Case-insensitive version of exact.
- contains: Field contains value.
- icontains: Case-insensitive version of contains.
- startswith: Field starts with value.
- istartswith: Case-insensitive version of startswith.
- endswith: Field ends with value.
- iendswith: Case-insensitive version of endswith.
- regex: Field matches the given regular expression.
- iregex: Case-insensitive version of regex.
- gt: Greater than comparison.
- gte: Greater than or equal to comparison.
- lt: Less than comparison.
- lte: Less than or equal to comparison.
- isnull: Check whether the given field or related object is null; expects a
  boolean value.
- in: Check whether the given field's value is present in the list provided;
  expects a list of items.
- Boolean values may be specified as True or 1 for true, False or 0 for false (both
  case-insensitive).

Null values may be specified as None or Null (both case-insensitive), though it is
preferred to use the isnull lookup to explicitly check for null values.

Lists (for the in lookup) may be specified as a comma-separated list of values.

Filtering based on the requesting user's level of access by query string parameter:

- role\_level: Level of role to filter on, such as admin\_role


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/pagination.html -->

## Limiting Response Results Using Pagination

The Oracle Linux Automation Manager REST API paginates responses for large collections
such as those that may contain tens or hundreds of thousands of objects. This causes
each web request to return only a limited number of results to prevent performance
degradation.

For example, the following shows the response results of a collection:

```
{'count': 25, 'next': 'http://testserver/api/v2/some_resource?page=2', 'previous': None, 'results': [ ... ] }
```

To get the next page, request the page given by the 'next' sequential URL.

You can change the number of results returned for each request with the page\_size query
string parameter . The default maximum limit for the page\_size parameter is 200 enforced
for values that exceed it, such as ?page\_size=1000. You can change this limit by setting
the value in /etc/tower/conf.d/<some file>.py to something higher, for example
MAX\_PAGE\_SIZE=1000.

Use the page query string parameter to retrieve a particular page of results.

```
http://<hostname or IP address>/api/v2/<multi_result_entity>?page_size=100&page=2
```

The previous and next links returned with the results sets these query string parameters
automatically. Request page sizes beyond a two hundred may experience performance
issues.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/configuration_settings.html -->

## Accessing Resources Using Named URLs

Oracle Linux Automation Manager provides two groups of named-URLs that you can use to
access and manage resources with. These named-URLs are located here:
/api/v2/settings/named-url/. The named-URL groups are:

- NAMED\_URL\_FORMATS
- NAMED\_URL\_GRAPH\_NODES

NAMED\_URL\_FORMATS is a read only key-value pair list of all available named URL
identifier formats. The NAMED\_URL\_FORMATS syntax is as follows:

- /organizations/<name>
- /teams/<name>++<organization.name>
- /credential\_types/<name>+<kind>
- /credentials/<name>++<credential\_type.name>+<credential\_type.kind>++<organization.name>
- /notification\_templates/<name>++<organization.name>
- /job\_templates/<name>++<organization.name>
- /projects/<name>++<organization.name>
- /inventories/<name>++<organization.name>
- /hosts/<name>++<inventory.name>++<organization.name>
- /groups/<name>++<inventory.name>++<organization.name>
- /inventory\_sources/<name>++<inventory.name>++<organization.name>
- /inventory\_scripts/<name>++<organization.name>
- /instance\_groups/<name>
- /labels/<name>++<organization.name>
- /workflow\_job\_templates/<name>++<organization.name>
- /workflow\_job\_template\_nodes/<identifier>++<workflow\_job\_template.name>++<organization.name>
- /applications/<name>++<organization.name>
- /users/<username>
- instances/<hostname>

For example, this cURL request returns details about the team1 that is part of
org1:

```
curl -i -H "Authorization: Bearer pVQoc51Apt4LNrXrNzoSbaMCDzjK8B" -X GET https://192.102.118.107/api/v2/teams/team1++org1/
```

NAMED\_URL\_FORMATS exclusively lists every resource that can have named URL. NAMED\_URL
resources each have a named\_url field which in the detailed view that represents the
object-specific named URL. You can also view an object's related URLs. For example, if
/api/v2/res\_name/obj\_slug/ is valid, /api/v2/res\_name/obj\_slug/related\_res\_name/ is
valid.

Every named URL resource has related field named\_url that displays that object's named
URL. You can copy and paste that field for your own use. For example, the following
shows team details with the ID 2 in the REST API browser at the /api/v2/teams/2/. In the
related object, the named\_url field shows the named url with a named\_url value:

```
"id": 2,
    "type": "team",
    "url": "/api/v2/teams/2/",
    "related": {
        "named_url": "/api/v2/teams/team2++org1/",
        "created_by": "/api/v2/users/1/",
....
```

An important aspect of generating a unique identifier for named URL has to do with
reserved characters. Because the identifier is part of a URL, the following reserved
characters are encoded by percentage symbols: ;/?:@=&[]. For example, if an
organization is named ;/?:@=&[], its unique identifier should be
%3B%2F%3F%3A%40%3D%26%5B%5D. Another special reserved character is +, which is not
reserved by URL standard but used by the named URL functionality to link different parts
of an identifier. It is encoded by [+]. For example, if an organization is named [+],
its unique identifier is %5B[+]%5D, where original [ and ] are percent encoded and + is
converted to [+].

NAMED\_URL\_GRAPH\_NODES is another read-only list of key-value pairs that exposes the
internal graph data structure that Oracle Linux Automation Manager uses to manage named
URLs. This is not intended to be human-readable but should be used for programmatically
generating named URLs. An example script for generating named URL given the primary key
of arbitrary resource objects that can have a named URL, using info provided by
NAMED\_URL\_GRAPH\_NODES, can be found in GitHub at <https://github.com/ansible/awx/blob/devel/tools/scripts/pk_to_named_url.py>.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/quick-start-cli.html -->

## Command-Line Interface Quick Start

Set up your environment and use the Command-Line Interface by performing these tasks.

Prerequisites

|  |  |
| --- | --- |
| Prerequisite | More Information |
| Install and start Oracle Linux Automation Manager. | See the [Oracle Linux Automation Manager Installation Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install2.3/) |
| Set Up the Command-Line Interface | [Setting Up the Command-Line Interface](use-cli.html "This section provides information about setting up the Oracle Linux Automation Manager Command Line Interface.") |
| Set up authentication | [Authenticating](authenticate.html) |
| Using the Command-Line Interface | [Using the Command-Line Interface](cli_intro.html) |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/use-cli.html -->

## Setting Up the Command-Line Interface

This section provides information about setting up the Oracle Linux Automation
Manager Command Line Interface.

Task 1: Install the Command-Line Interface

You can install the Command-Line interface on the same system as the Oracle Linux
Automation Manager server or a different Oracle Linux 8 or 9 system that can connect
to the Oracle Linux Automation Manager server.

The following procedure describes how to setup your Oracle Linux 8 or 9 system to
install the Oracle Linux Automation Manager Command-Line Interface:

1. Setup the Oracle Linux Automation Manager server as described in [Oracle Linux Automation Manager Installation Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install2.3/).
2. If you are running the CLI on a different machine running Oracle Linux 8 or 9, enable
   the DNF repositories or the ULN channels as described in [Oracle Linux Automation Manager Installation Guide](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/install2.3/).
3. On the same machine running the Oracle Linux Automation Manager server or on a
   different machine, install the ol-automation-manager-cli package.

   ```
   sudo dnf install ol-automation-manager-cli
   ```
4. Ensure the machine you are using can access the ports setup on Oracle Linux
   Automation Manager.

Task 2: Run a Command-Line Interface Command

Run a command-line interface command and specify one or more of the command-line
options. For example,

1. Obtain an authentication token for the user account you want to use the
   command-line interface. For more information about obtaining a token
   authentication, see [Authenticating](authenticate.html).
2. From a terminal on your system, use the following syntax:

   ```
   awx --conf.host https://<hostname or IP address> --conf.token <access_token> <resource> <action> <optional_arguments> <input/output formatting>
   ```

   In
   the previous syntax,

   - <hostname or IP address> is the hostname or IP address of the
     Oracle Linux Automation Manager server,
   - <access\_token> is an Oauth2 token,
   - <resource> is a resource on which to perform an action,
   - <action> is an action to be performed on a resource,
   - <optional\_arguments> are any further options to be specified
     for the action,
   - <input/output formatting> is any extra formatting options to
     be applied to the response

   For more information about these parameters, see [Using the Command-Line Interface](cli_intro.html).

   For example, the following command lists
   all users configured on an Oracle Linux Automation Manager server:

   ```
   awx --conf.host https://192.102.118.107 --conf.token h7a3NPiam8Or4px7Kkoe87cWcTeixz users list
   {
        "count": 3,
        "next": null,
        "previous": null,
        "results": [
             {
                  "id": 1,
                  "type": "user",
                  "url": "/api/v2/users/1/",
                  "related": {
                       "teams": "/api/v2/users/1/teams/",
                       "organizations": "/api/v2/users/1/organizations/",
                       "admin_of_organizations": "/api/v2/users/1/admin_of_organizations/",
                       "projects": "/api/v2/users/1/projects/",
                       "credentials": "/api/v2/users/1/credentials/",
                       "roles": "/api/v2/users/1/roles/",
                       "activity_stream": "/api/v2/users/1/activity_stream/",
                       "access_list": "/api/v2/users/1/access_list/",
                       "tokens": "/api/v2/users/1/tokens/",
                       "authorized_tokens": "/api/v2/users/1/authorized_tokens/",
                       "personal_tokens": "/api/v2/users/1/personal_tokens/"
                  },
                  "summary_fields": {
                       "user_capabilities": {
                            "edit": true,
                            "delete": false
                       }
                  },
                  "created": "2024-08-12T16:46:26.217924Z",
                  "modified": "2024-08-12T16:48:34.750654Z",
                  "username": "admin",

   ....
   ```


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/authenticate-01.html -->

## Authenticating

Oracle Linux Automation Manager uses a certificate authority (CA) certificate with NGINX
and Oauth2 for token based authentication to enable clients to connect securely to the
server. Tokens are easily revoked and are best suited to third-party tooling
integration.

Note:

The Oracle Linux Automation Manager Installation Guide document provides
instructions for setting up the server with a self-signed certificate, however, we
recommend that you use a signed certificate to ensure the server is secure. If you
use the self-signed certificate, then append `-k` to all Oracle Linux
Automation Manager REST API curl or CLI requests to indicate that the request is
insecure.

To setup an Oauth2 token for a user, do the following:

1. Open a terminal on the Oracle Linux Automation Manager server.
2. Run the following commands:

   ```
   sudo su -l awx -s /bin/bash
   awx-manage create_oauth2_token --user=<username>
   ```

   In the previous example,
   <username> is the user name of the account for which you want to create a token.
3. The command generates a token that you must note down in a secure way so that you
   can use it when running cURL or CLI commands. For example, the following token is
   generated using the create\_oauth2\_token command:

   ```
   JWjb1AyOJOWi4yPBYWC7NQofdNSjAM
   ```

To revoke all Oauth2 token for a user, do the following:

1. Open a terminal on the Oracle Linux Automation Manager server.
2. Run the following commands:

   ```
   sudo su -l awx -s /bin/bash
   awx-manage revoke_oauth2_tokens --user=<username>
   ```

   In the previous example,
   <username> is the user name of the account for which you want to revoke all
   tokens. The command lists all revoked tokens for the user. For example, the
   following tokens are revoked when using the revoke\_token2\_tokens command:

   ```
   revoked OAuth2AccessToken aeOy7IWqlt19Kc8Fu1IElsj2w6rCOz
   revoked OAuth2AccessToken JWjb1AyOJOWi4yPBYWC7NQofdNSjAM
   ```


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/cli_intro.html -->

## Using the Command-Line Interface

The awx command is used to configure, deploy and manage the resources in Oracle
Linux Automation Manager. The awx command is installed using the
ol-automation-manager-cli package on an Oracle Linux Automation Manager server or any
Oracle Linux 8 or 9 system that can connect to the server. For information about setting up an
Oracle Linux Automation Server, see the [Oracle Linux Automation Manager](https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/) documentation.

You interact with awx by entering commands with a series of options. The awx
command alone returns the following syntax information:

```
awx
usage: awx [--help] [--version] [--conf.host https://<host or IP address>]
           [--conf.token TEXT] [--conf.username TEXT] [--conf.password TEXT]
           [-k] [-f {json,yaml,jq,human}] [--filter TEXT]
           [--conf.color BOOLEAN] [-v]

optional arguments:
  --help                prints usage information for the awx tool
  --version             display awx CLI version

authentication:
  --conf.host https://example.awx.org
  --conf.token TEXT     an OAuth2.0 token (get one by using 'awx login')
  --conf.username TEXT
  --conf.password TEXT
  -k, --conf.insecure   Allow insecure server connections when using SSL

input/output formatting:
  -f {json,yaml,jq,human}, --conf.format {json,yaml,jq,human}
                        specify a format for the input and output
  --filter TEXT         specify an output filter (only valid with jq or human
                        format)
  --conf.color BOOLEAN  Display colorized output. Defaults to True
  -v, --verbose         print debug-level logs, including requests made
```

The usage section lists the position of options when used. These options are defined in
the optional arguments:, authentication:, and input/output formatting:
sections.

When you use the awx command, you are prompted for any missing options.

Getting Syntax Help

You can get help on the syntax for awx commands using the --help option. For
example, the following shows the resources options available for the awx command:

Note:

The commands in this section require that you connect to an
Oracle Linux Automation Manager server. For more information about connecting to an Oracle
Linux Automation Manager server with the command-line tool, see [Using the Command-Line Interface](cli_intro.html).

```
awx --conf.host https://192.102.118.107 --conf.token 0AlhUsyKqXwBAEmNerwlcqB6a3aRlP --help
usage: awx [--help] [--version] [--conf.host https://example.awx.org]
           [--conf.token TEXT] [--conf.username TEXT] [--conf.password TEXT]
           [-k] [-f {json,yaml,jq,human}] [--filter TEXT]
           [--conf.color BOOLEAN] [-v]
           resource ...

positional arguments:
  resource
    login               authenticate and retrieve an OAuth2 token
    config              print current configuration values
    import              import resources into Tower
    export              export resources from Tower
    ping
    instances (instance)
    instance_groups (instance_group)
    config
    settings (setting)
    me
    organizations (organization)
    users (user)
    projects (project)
    project_updates (project_update)
    teams (team)
    credentials (credential)
    credential_types (credential_type)
    credential_input_sources
    applications (application)
    tokens
    metrics
    inventory (inventories)
    inventory_scripts (inventory_script)
    inventory_sources (inventory_source)
    inventory_updates (inventory_update)
    groups (group)
    hosts (host)
    job_templates (job_template)
    jobs (job)
    job_events
    ad_hoc_commands (ad_hoc)
    system_job_templates
    system_jobs
    schedules (schedule)
    roles (role)
    notification_templates (notification_template)
    notifications
    labels (label)
    unified_job_templates
    unified_jobs
    activity_stream
    workflow_job_templates (workflow)
    workflow_jobs (workflow_job)
    workflow_approvals
    workflow_job_template_nodes (node)
    workflow_job_nodes
```

The Positional arguments section lists any available resources for the awx
command. You can obtain further information about these resources by adding them to the
command followed by the --help option. For example, the following command shows the
available actions for the users resource:

```
awx --conf.host https://192.102.118.107 --conf.token h7a3NPiam8Or4px7Kkoe87cWcTeixz users --help
usage: awx users [-h] action ...

positional arguments:
  action
    list
    create
    get
    modify
    delete
    grant
    revoke

optional arguments:
  -h, --help  show this help message and exit

awx users: the following arguments are required: action
```

You can then add the action to the command and generate additional help text using
--help. For example, the following shows additional options for the list action
that are specific to the users resource:

```
awx --conf.host https://192.102.118.107 --conf.token h7a3NPiam8Or4px7Kkoe87cWcTeixz users list --help
usage: awx users list [-h] [--all] [-f {json,yaml,jq,human}] [--filter TEXT]
                      [--conf.color BOOLEAN] [-v] [--type {user}]
                      [--username TEXT] [--first_name TEXT] [--last_name TEXT]
                      [--email TEXT] [--is_superuser BOOLEAN]
                      [--last_login LAST_LOGIN]

optional arguments:
  -h, --help            show this help message and exit
  --all                 fetch all pages of content from the API when returning
                        results (instead of just the first page)
  --type {user}         only list users with the specified type
  --username TEXT       only list users with the specified username
  --first_name TEXT     only list users with the specified first_name
  --last_name TEXT      only list users with the specified last_name
  --email TEXT          only list users with the specified email
  --is_superuser BOOLEAN
                        only list users with the specified is_superuser
  --last_login LAST_LOGIN
                        only list users with the specified last_login

input/output formatting:
  -f {json,yaml,jq,human}, --conf.format {json,yaml,jq,human}
                        specify a format for the input and output
  --filter TEXT         specify an output filter (only valid with jq or human
                        format)
  --conf.color BOOLEAN  Display colorized output. Defaults to True
  -v, --verbose         print debug-level logs, including requests made
```

The optional arguments: returned from this command lists additional ways to filter
results.

With the information obtained using the --help option, you now have the information
you need to search through all users configured on your Oracle Linux Automation Manager
server to find the one you are looking for. For example, the following command displays user
information for the username johnsmith

```
.awx --conf.host https://192.102.118.107 --conf.token h7a3NPiam8Or4px7Kkoe87cWcTeixz users list --username johnsmith
{
     "count": 1,
     "next": null,
     "previous": null,
     "results": [
          {
               "id": 3,
               "type": "user",
               "url": "/api/v2/users/3/",
               "related": {
                    "teams": "/api/v2/users/3/teams/",
                    "organizations": "/api/v2/users/3/organizations/",
                    "admin_of_organizations": "/api/v2/users/3/admin_of_organizations/",
                    "projects": "/api/v2/users/3/projects/",
                    "credentials": "/api/v2/users/3/credentials/",
                    "roles": "/api/v2/users/3/roles/",
                    "activity_stream": "/api/v2/users/3/activity_stream/",
                    "access_list": "/api/v2/users/3/access_list/",
                    "tokens": "/api/v2/users/3/tokens/",
                    "authorized_tokens": "/api/v2/users/3/authorized_tokens/",
                    "personal_tokens": "/api/v2/users/3/personal_tokens/"
               },
               "summary_fields": {
                    "user_capabilities": {
                         "edit": true,
                         "delete": true
                    }
               },
               "created": "2021-11-12T16:11:37.315560Z",
               "username": "johnssmith",
               "first_name": "John",
               "last_name": "Smith",
               "email": "example@example.com",
               "is_superuser": false,
               "is_system_auditor": true,
               "ldap_dn": "",
               "last_login": "2021-11-12T16:14:47.532042Z",
               "external_account": null,
               "auth": []
          }
     ]
}
```


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/reference.html -->

## Reference

Here is some additional reference information to help you work with REST
APIs:

Topics:

- [Exporting Data](use-case-name.html "You can export data from Oracle Linux Automation Manager using the command-line interface.")
- [Importing Data](use-case-import.html "You can import data to Oracle Linux Automation Manager using the command-line interface with data files previously exported or created manually.")


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/use-case-name.html -->

## Exporting Data

You can export data from Oracle Linux Automation Manager using the command-line
interface.

This task is commonly done to backup your Oracle Linux Automation Manager server.
This use case requires that you have installed the command-line interface and have
configured an Oauth2 token for your account.

To export data to a json file from Oracle Linux Automation Manager, do the
following:

1. Generate the list of resources you want to export.

   ```
   awx --conf.host https://192.102.118.107 --conf.token h7a3NPiam8Or4px7Kkoe87cWcTeixz --help
   ```

   Specify the following options on the command-line interface:

   - `--conf.host` option to include the HTTPS address of
     your Oracle Linux Automation Server IP address or hostname.
   - `--conf.token` option to include the Oauth2 token.
   - `--help` option to generate help information.
2. Do a partial export of a resource. For example, you can export all users
   information by entering the following command.

   ```
   awx --conf.host https://192.102.118.107 --conf.token h7a3NPiam8Or4px7Kkoe87cWcTeixz export --users > users.json
   ```

   The export command followed by the --users resource type generates an export
   of all user to the users.json file.
3. Do a full export of all resources on your system. For example, enter the
   following command:

   ```
   awx --conf.host https://192.102.118.107 --conf.token h7a3NPiam8Or4px7Kkoe87cWcTeixz export > all_resources.json
   ```

   When the export command is used without any resources specified exports all
   resources to the all\_resources.json file.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/use-case-import.html -->

## Importing Data

You can import data to Oracle Linux Automation Manager using the command-line
interface with data files previously exported or created manually.

This task is commonly done to restore your Oracle Linux Automation Manager server.
This use case requires that you have installed the command-line interface, have
configured an Oauth2 token for your account and have exported or manually created
files with resources ready to import.

To import data from a json file to Oracle Linux Automation Manager, do the
following:

1. Do an import of a resource defined in a json file. For example, you can import
   all users information contained in a json file by entering the following
   command.

   ```
   awx --conf.host https://192.102.118.107 --conf.token h7a3NPiam8Or4px7Kkoe87cWcTeixz import --users < users.json
   ```

   Specify the following options on the command-line interface:

   - `--conf.host` option to include the HTTPS address of
     your Oracle Linux Automation Server IP address or hostname.
   - `--conf.token` option to include the Oauth2 token.
   - `import` option specifies the import action.
   - `--users` option specifies the users resource.
   - `< users.json` is the file containing the user account
     information to be imported.

     Note:

     For each user
     being imported, add the user's password to the
     `password` field.
2. Do a full import of all resources from a backup file. For example, enter the
   following command:

   ```
   awx --conf.host https://192.102.118.107 --conf.token h7a3NPiam8Or4px7Kkoe87cWcTeixz import < all_resources.json
   ```

   When the import command is used without any resources specified, the command
   imports all resources to the all\_resources.json file.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/api-activity-stream.html -->

Sort by

Task

 Path

 Method

Activity Stream

REST API endpoints for Activity Stream

[List Activity Streams](op-api-v2-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/activity_stream/`

[Retrieve an Activity Stream](op-api-v2-activity_stream-id-get.html)
:   Method: get

    Path: `/api/v2/activity_stream/{id}/`


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-activity_stream-get.html -->

Make a GET request to this resource to retrieve the list of
activity streams.

The resulting data structure contains:

```
{
    "count": 99,
    "next": null,
    "previous": null,
    "results": [
        ...
    ]
}
```

The `count` field indicates the total number of activity streams
found for the given query. The `next` and `previous` fields provides links to
additional results if there are more than will fit on a single page. The
`results` list contains zero or more activity stream records.

## Results

Each activity stream data structure includes the following fields:

- `id`: Database ID for this activity stream. (integer)
- `type`: Data type for this activity stream. (choice)
- `url`: URL for this activity stream. (string)
- `related`: Data structure with URLs of related resources. (object)
- `summary_fields`: Data structure with name/description for related resources. The output for some objects may be limited for performance reasons. (object)
- `timestamp`: (datetime)
- `operation`: The action taken with respect to the given object(s). (choice)
  - `create`: Entity Created
  - `update`: Entity Updated
  - `delete`: Entity Deleted
  - `associate`: Entity Associated with another Entity
  - `disassociate`: Entity was Disassociated with another Entity
- `changes`: A summary of the new and changed values when an object is created, updated, or deleted (json)
- `object1`: For create, update, and delete events this is the object type that was affected. For associate and disassociate events this is the object type associated or disassociated with object2. (string)
- `object2`: Unpopulated for create, update, and delete events. For associate and disassociate events this is the object type that object1 is being associated with. (string)
- `object_association`: When present, shows the field name of the role or relationship that changed. (field)
- `action_node`: The cluster node the activity took place on. (string)
- `object_type`: When present, shows the model on which the role or relationship was defined. (field)

## Sorting

To specify that activity streams are returned in a particular
order, use the `order_by` query string parameter on the GET request.

```
?order_by=
```

Prefix the field name with a dash `-` to sort in reverse:

```
?order_by=-
```

Multiple sorting fields may be specified by separating the field names with a
comma `,`:

```
?order_by=,some_other_field
```

## Pagination

Use the `page_size` query string parameter to change the number of results
returned for each request. Use the `page` query string parameter to retrieve
a particular page of results.

```
?page_size=100&page=2
```

The `previous` and `next` links returned with the results will set these query
string parameters automatically.

## Searching

Use the `search` query string parameter to perform a case-insensitive search
within all designated text fields of a model.

```
?search=findme
```

(*Added in Ansible Tower 3.1.0*) Search across related fields:

```
?related__search=findme
```

### Request

Supported Media Types

- application/json

Query Parameters

- [page: integer](#request-query-param-0)

  A page number within the paginated result set.
- [page\_size: integer](#request-query-param-1)

  Number of results to return per page.
- [search: string](#request-query-param-2)

  A search term.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

Body ()

Root Schema : schema

Type: `object`

[Show Source](#)

- [count(required):
  integer](#200-paths--api-v2-activity_stream--get-responses-200-schema-properties-count-properties-count-0)
- [next:
  string(uri)](#200-paths--api-v2-activity_stream--get-responses-200-schema-properties-next-properties-next-0)
- [previous:
  string(uri)](#200-paths--api-v2-activity_stream--get-responses-200-schema-properties-previous-properties-previous-0)
- [results(required):
  array](#200-paths--api-v2-activity_stream--get-responses-200-schema-properties-results-properties-results-0)  [results](#200-paths--api-v2-activity_stream--get-responses-200-schema-properties-results)

```
{
    "properties":{
        "count":{
            "type":"integer"
        },
        "next":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "previous":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "results":{
            "items":{
                "$ref":"#/definitions/ActivityStream"
            },
            "type":"array"
        }
    },
    "required":[
        "count",
        "results"
    ],
    "type":"object"
}
```

Nested Schema : results

Type: `array`

[Show Source](#)

- [Array of:
  object](#200-definitions-ActivityStream-items-0)  [ActivityStream](#200-definitions-ActivityStream)

```
{
    "items":{
        "$ref":"#/definitions/ActivityStream"
    },
    "type":"array"
}
```

Nested Schema : ActivityStream

Type: `object`

[Show Source](#)

- [action\_node:
  string](#200-definitions-ActivityStream-properties-action_node-properties-action_node-0)

  Title: `Action node`

  Read Only: `true`

  Minimum Length: `1`

  The cluster node the activity took place on.
- [changes:
  string](#200-definitions-ActivityStream-properties-changes-properties-changes-0)

  Title: `Changes`

  Read Only: `true`

  A summary of the new and changed values when an object is created, updated, or deleted
- [id:
  integer](#200-definitions-ActivityStream-properties-id-properties-id-0)

  Title: `ID`

  Read Only: `true`
- [object1(required):
  string](#200-definitions-ActivityStream-properties-object1-properties-object1-0)

  Title: `Object1`

  Minimum Length: `1`

  For create, update, and delete events this is the object type that was affected. For associate and disassociate events this is the object type associated or disassociated with object2.
- [object2(required):
  string](#200-definitions-ActivityStream-properties-object2-properties-object2-0)

  Title: `Object2`

  Minimum Length: `1`

  Unpopulated for create, update, and delete events. For associate and disassociate events this is the object type that object1 is being associated with.
- [object\_association:
  string](#200-definitions-ActivityStream-properties-object_association-properties-object_association-0)

  Title: `Object association`

  Read Only: `true`

  When present, shows the field name of the role or relationship that changed.
- [object\_type:
  string](#200-definitions-ActivityStream-properties-object_type-properties-object_type-0)

  Title: `Object type`

  Read Only: `true`

  When present, shows the model on which the role or relationship was defined.
- [operation(required):
  string](#200-definitions-ActivityStream-properties-operation-properties-operation-0)

  Title: `Operation`

  Allowed Values: `[
  "create",
  "update",
  "delete",
  "associate",
  "disassociate"
  ]`

  The action taken with respect to the given object(s).
- [related:
  string](#200-definitions-ActivityStream-properties-related-properties-related-0)

  Title: `Related`

  Read Only: `true`
- [summary\_fields:
  string](#200-definitions-ActivityStream-properties-summary_fields-properties-summary_fields-0)

  Title: `Summary fields`

  Read Only: `true`
- [timestamp:
  string(date-time)](#200-definitions-ActivityStream-properties-timestamp-properties-timestamp-0)

  Title: `Timestamp`

  Read Only: `true`
- [type:
  string](#200-definitions-ActivityStream-properties-type-properties-type-0)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#200-definitions-ActivityStream-properties-url-properties-url-0)

  Title: `Url`

  Read Only: `true`

```
{
    "properties":{
        "action_node":{
            "description":"The cluster node the activity took place on.",
            "minLength":"1",
            "readOnly":true,
            "title":"Action node",
            "type":"string"
        },
        "changes":{
            "description":"A summary of the new and changed values when an object is created, updated, or deleted",
            "readOnly":true,
            "title":"Changes",
            "type":"string"
        },
        "id":{
            "readOnly":true,
            "title":"ID",
            "type":"integer"
        },
        "object1":{
            "description":"For create, update, and delete events this is the object type that was affected. For associate and disassociate events this is the object type associated or disassociated with object2.",
            "minLength":"1",
            "title":"Object1",
            "type":"string",
            "x-nullable":true
        },
        "object2":{
            "description":"Unpopulated for create, update, and delete events. For associate and disassociate events this is the object type that object1 is being associated with.",
            "minLength":"1",
            "title":"Object2",
            "type":"string",
            "x-nullable":true
        },
        "object_association":{
            "description":"When present, shows the field name of the role or relationship that changed.",
            "readOnly":true,
            "title":"Object association",
            "type":"string"
        },
        "object_type":{
            "description":"When present, shows the model on which the role or relationship was defined.",
            "readOnly":true,
            "title":"Object type",
            "type":"string"
        },
        "operation":{
            "description":"The action taken with respect to the given object(s).",
            "enum":[
                "create",
                "update",
                "delete",
                "associate",
                "disassociate"
            ],
            "title":"Operation",
            "type":"string",
            "x-nullable":true
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "timestamp":{
            "format":"date-time",
            "readOnly":true,
            "title":"Timestamp",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        }
    },
    "required":[
        "operation",
        "object1",
        "object2"
    ],
    "type":"object"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-activity_stream-id-get.html -->

Make GET request to this resource to retrieve a single activity stream
record containing the following fields:

- `id`: Database ID for this activity stream. (integer)
- `type`: Data type for this activity stream. (choice)
- `url`: URL for this activity stream. (string)
- `related`: Data structure with URLs of related resources. (object)
- `summary_fields`: Data structure with name/description for related resources. The output for some objects may be limited for performance reasons. (object)
- `timestamp`: (datetime)
- `operation`: The action taken with respect to the given object(s). (choice)
  - `create`: Entity Created
  - `update`: Entity Updated
  - `delete`: Entity Deleted
  - `associate`: Entity Associated with another Entity
  - `disassociate`: Entity was Disassociated with another Entity
- `changes`: A summary of the new and changed values when an object is created, updated, or deleted (json)
- `object1`: For create, update, and delete events this is the object type that was affected. For associate and disassociate events this is the object type associated or disassociated with object2. (string)
- `object2`: Unpopulated for create, update, and delete events. For associate and disassociate events this is the object type that object1 is being associated with. (string)
- `object_association`: When present, shows the field name of the role or relationship that changed. (field)
- `action_node`: The cluster node the activity took place on. (string)
- `object_type`: When present, shows the model on which the role or relationship was defined. (field)

### Request

Supported Media Types

- application/json

Path Parameters

- [id(required): string](#request-path-param-0)

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

Body ()

Root Schema : ActivityStream

Type: `object`

[Show Source](#)

- [action\_node:
  string](#200-definitions-ActivityStream-properties-action_node-properties-action_node-1)

  Title: `Action node`

  Read Only: `true`

  Minimum Length: `1`

  The cluster node the activity took place on.
- [changes:
  string](#200-definitions-ActivityStream-properties-changes-properties-changes-1)

  Title: `Changes`

  Read Only: `true`

  A summary of the new and changed values when an object is created, updated, or deleted
- [id:
  integer](#200-definitions-ActivityStream-properties-id-properties-id-1)

  Title: `ID`

  Read Only: `true`
- [object1(required):
  string](#200-definitions-ActivityStream-properties-object1-properties-object1-1)

  Title: `Object1`

  Minimum Length: `1`

  For create, update, and delete events this is the object type that was affected. For associate and disassociate events this is the object type associated or disassociated with object2.
- [object2(required):
  string](#200-definitions-ActivityStream-properties-object2-properties-object2-1)

  Title: `Object2`

  Minimum Length: `1`

  Unpopulated for create, update, and delete events. For associate and disassociate events this is the object type that object1 is being associated with.
- [object\_association:
  string](#200-definitions-ActivityStream-properties-object_association-properties-object_association-1)

  Title: `Object association`

  Read Only: `true`

  When present, shows the field name of the role or relationship that changed.
- [object\_type:
  string](#200-definitions-ActivityStream-properties-object_type-properties-object_type-1)

  Title: `Object type`

  Read Only: `true`

  When present, shows the model on which the role or relationship was defined.
- [operation(required):
  string](#200-definitions-ActivityStream-properties-operation-properties-operation-1)

  Title: `Operation`

  Allowed Values: `[
  "create",
  "update",
  "delete",
  "associate",
  "disassociate"
  ]`

  The action taken with respect to the given object(s).
- [related:
  string](#200-definitions-ActivityStream-properties-related-properties-related-1)

  Title: `Related`

  Read Only: `true`
- [summary\_fields:
  string](#200-definitions-ActivityStream-properties-summary_fields-properties-summary_fields-1)

  Title: `Summary fields`

  Read Only: `true`
- [timestamp:
  string(date-time)](#200-definitions-ActivityStream-properties-timestamp-properties-timestamp-1)

  Title: `Timestamp`

  Read Only: `true`
- [type:
  string](#200-definitions-ActivityStream-properties-type-properties-type-1)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#200-definitions-ActivityStream-properties-url-properties-url-1)

  Title: `Url`

  Read Only: `true`

```
{
    "properties":{
        "action_node":{
            "description":"The cluster node the activity took place on.",
            "minLength":"1",
            "readOnly":true,
            "title":"Action node",
            "type":"string"
        },
        "changes":{
            "description":"A summary of the new and changed values when an object is created, updated, or deleted",
            "readOnly":true,
            "title":"Changes",
            "type":"string"
        },
        "id":{
            "readOnly":true,
            "title":"ID",
            "type":"integer"
        },
        "object1":{
            "description":"For create, update, and delete events this is the object type that was affected. For associate and disassociate events this is the object type associated or disassociated with object2.",
            "minLength":"1",
            "title":"Object1",
            "type":"string",
            "x-nullable":true
        },
        "object2":{
            "description":"Unpopulated for create, update, and delete events. For associate and disassociate events this is the object type that object1 is being associated with.",
            "minLength":"1",
            "title":"Object2",
            "type":"string",
            "x-nullable":true
        },
        "object_association":{
            "description":"When present, shows the field name of the role or relationship that changed.",
            "readOnly":true,
            "title":"Object association",
            "type":"string"
        },
        "object_type":{
            "description":"When present, shows the model on which the role or relationship was defined.",
            "readOnly":true,
            "title":"Object type",
            "type":"string"
        },
        "operation":{
            "description":"The action taken with respect to the given object(s).",
            "enum":[
                "create",
                "update",
                "delete",
                "associate",
                "disassociate"
            ],
            "title":"Operation",
            "type":"string",
            "x-nullable":true
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "timestamp":{
            "format":"date-time",
            "readOnly":true,
            "title":"Timestamp",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        }
    },
    "required":[
        "operation",
        "object1",
        "object2"
    ],
    "type":"object"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/api-ad-hoc-command-events.html -->

Sort by

Task

 Path

 Method

Ad Hoc Command Events

REST API endpoints for Ad Hoc Command Events

[Retrieve an Ad Hoc Command Event](op-api-v2-ad_hoc_command_events-id-get.html)
:   Method: get

    Path: `/api/v2/ad_hoc_command_events/{id}/`


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-ad_hoc_command_events-id-get.html -->

Make GET request to this resource to retrieve a single ad hoc command event
record containing the following fields:

- `id`: Database ID for this ad hoc command event. (integer)
- `type`: Data type for this ad hoc command event. (choice)
- `url`: URL for this ad hoc command event. (string)
- `related`: Data structure with URLs of related resources. (object)
- `summary_fields`: Data structure with name/description for related resources. The output for some objects may be limited for performance reasons. (object)
- `created`: Timestamp when this ad hoc command event was created. (datetime)
- `modified`: Timestamp when this ad hoc command event was last modified. (datetime)
- `ad_hoc_command`: (id)
- `event`: (choice)
  - `runner_on_failed`: Host Failed
  - `runner_on_ok`: Host OK
  - `runner_on_unreachable`: Host Unreachable
  - `runner_on_skipped`: Host Skipped
  - `debug`: Debug
  - `verbose`: Verbose
  - `deprecated`: Deprecated
  - `warning`: Warning
  - `system_warning`: System Warning
  - `error`: Error
- `counter`: (integer)
- `event_display`: (string)
- `event_data`: (json)
- `failed`: (boolean)
- `changed`: (boolean)
- `uuid`: (string)
- `host`: (id)
- `host_name`: (string)
- `stdout`: (string)
- `start_line`: (integer)
- `end_line`: (integer)
- `verbosity`: (integer)

### Request

Supported Media Types

- application/json

Path Parameters

- [id(required): string](#request-path-param-0)

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

Body ()

Root Schema : AdHocCommandEvent

Type: `object`

[Show Source](#)

- [ad\_hoc\_command:
  string](#200-definitions-AdHocCommandEvent-properties-ad_hoc_command-properties-ad_hoc_command-0)

  Title: `Ad hoc command`

  Read Only: `true`
- [changed:
  boolean](#200-definitions-AdHocCommandEvent-properties-changed-properties-changed-0)

  Title: `Changed`

  Read Only: `true`
- [counter:
  integer](#200-definitions-AdHocCommandEvent-properties-counter-properties-counter-0)

  Title: `Counter`

  Read Only: `true`

  Minimum Value: `0`
- [created:
  string](#200-definitions-AdHocCommandEvent-properties-created-properties-created-0)

  Title: `Created`

  Read Only: `true`
- [end\_line:
  integer](#200-definitions-AdHocCommandEvent-properties-end_line-properties-end_line-0)

  Title: `End line`

  Read Only: `true`

  Minimum Value: `0`
- [event(required):
  string](#200-definitions-AdHocCommandEvent-properties-event-properties-event-0)

  Title: `Event`

  Allowed Values: `[
  "runner_on_failed",
  "runner_on_ok",
  "runner_on_unreachable",
  "runner_on_skipped",
  "debug",
  "verbose",
  "deprecated",
  "warning",
  "system_warning",
  "error"
  ]`
- [event\_data:
  object](#200-definitions-AdHocCommandEvent-properties-event_data-properties-event_data-0)  [Event data](#200-definitions-AdHocCommandEvent-properties-event_data)

  Title: `Event data`
- [event\_display:
  string](#200-definitions-AdHocCommandEvent-properties-event_display-properties-event_display-0)

  Title: `Event display`

  Read Only: `true`

  Minimum Length: `1`
- [failed:
  boolean](#200-definitions-AdHocCommandEvent-properties-failed-properties-failed-0)

  Title: `Failed`

  Read Only: `true`
- [host:
  integer](#200-definitions-AdHocCommandEvent-properties-host-properties-host-0)

  Title: `Host`

  Read Only: `true`
- [host\_name:
  string](#200-definitions-AdHocCommandEvent-properties-host_name-properties-host_name-0)

  Title: `Host name`

  Read Only: `true`

  Minimum Length: `1`
- [id:
  integer](#200-definitions-AdHocCommandEvent-properties-id-properties-id-0)

  Title: `ID`

  Read Only: `true`
- [modified:
  string](#200-definitions-AdHocCommandEvent-properties-modified-properties-modified-0)

  Title: `Modified`

  Read Only: `true`
- [related:
  string](#200-definitions-AdHocCommandEvent-properties-related-properties-related-0)

  Title: `Related`

  Read Only: `true`
- [start\_line:
  integer](#200-definitions-AdHocCommandEvent-properties-start_line-properties-start_line-0)

  Title: `Start line`

  Read Only: `true`

  Minimum Value: `0`
- [stdout:
  string](#200-definitions-AdHocCommandEvent-properties-stdout-properties-stdout-0)

  Title: `Stdout`

  Read Only: `true`

  Minimum Length: `1`
- [summary\_fields:
  string](#200-definitions-AdHocCommandEvent-properties-summary_fields-properties-summary_fields-0)

  Title: `Summary fields`

  Read Only: `true`
- [type:
  string](#200-definitions-AdHocCommandEvent-properties-type-properties-type-0)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#200-definitions-AdHocCommandEvent-properties-url-properties-url-0)

  Title: `Url`

  Read Only: `true`
- [uuid:
  string](#200-definitions-AdHocCommandEvent-properties-uuid-properties-uuid-0)

  Title: `Uuid`

  Read Only: `true`

  Minimum Length: `1`
- [verbosity:
  integer](#200-definitions-AdHocCommandEvent-properties-verbosity-properties-verbosity-0)

  Title: `Verbosity`

  Read Only: `true`

  Minimum Value: `0`

```
{
    "properties":{
        "ad_hoc_command":{
            "readOnly":true,
            "title":"Ad hoc command",
            "type":"string"
        },
        "changed":{
            "readOnly":true,
            "title":"Changed",
            "type":"boolean"
        },
        "counter":{
            "minimum":"0",
            "readOnly":true,
            "title":"Counter",
            "type":"integer"
        },
        "created":{
            "readOnly":true,
            "title":"Created",
            "type":"string"
        },
        "end_line":{
            "minimum":"0",
            "readOnly":true,
            "title":"End line",
            "type":"integer"
        },
        "event":{
            "enum":[
                "runner_on_failed",
                "runner_on_ok",
                "runner_on_unreachable",
                "runner_on_skipped",
                "debug",
                "verbose",
                "deprecated",
                "warning",
                "system_warning",
                "error"
            ],
            "title":"Event",
            "type":"string",
            "x-nullable":true
        },
        "event_data":{
            "title":"Event data",
            "type":"object"
        },
        "event_display":{
            "minLength":"1",
            "readOnly":true,
            "title":"Event display",
            "type":"string"
        },
        "failed":{
            "readOnly":true,
            "title":"Failed",
            "type":"boolean"
        },
        "host":{
            "readOnly":true,
            "title":"Host",
            "type":"integer",
            "x-nullable":true
        },
        "host_name":{
            "minLength":"1",
            "readOnly":true,
            "title":"Host name",
            "type":"string"
        },
        "id":{
            "readOnly":true,
            "title":"ID",
            "type":"integer"
        },
        "modified":{
            "readOnly":true,
            "title":"Modified",
            "type":"string"
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "start_line":{
            "minimum":"0",
            "readOnly":true,
            "title":"Start line",
            "type":"integer"
        },
        "stdout":{
            "minLength":"1",
            "readOnly":true,
            "title":"Stdout",
            "type":"string"
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        },
        "uuid":{
            "minLength":"1",
            "readOnly":true,
            "title":"Uuid",
            "type":"string"
        },
        "verbosity":{
            "minimum":"0",
            "readOnly":true,
            "title":"Verbosity",
            "type":"integer"
        }
    },
    "required":[
        "event"
    ],
    "type":"object"
}
```

Nested Schema : Event data

Type: `object`

Title: `Event data`

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/api-ad-hoc-commands.html -->

Sort by

Task

 Path

 Method

Ad Hoc Commands

REST API endpoints for Ad Hoc Commands

[Create an Ad Hoc Command](op-api-v2-ad_hoc_commands-post.html)
:   Method: post

    Path: `/api/v2/ad_hoc_commands/`

[Delete an Ad Hoc Command](op-api-v2-ad_hoc_commands-id-delete.html)
:   Method: delete

    Path: `/api/v2/ad_hoc_commands/{id}/`

[List Activity Streams for an Ad Hoc Command](op-api-v2-ad_hoc_commands-id-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/ad_hoc_commands/{id}/activity_stream/`

[List Ad Hoc Command Events for an Ad Hoc Command](op-api-v2-ad_hoc_commands-id-events-get.html)
:   Method: get

    Path: `/api/v2/ad_hoc_commands/{id}/events/`

[List Ad Hoc Commands](op-api-v2-ad_hoc_commands-get.html)
:   Method: get

    Path: `/api/v2/ad_hoc_commands/`

[List Notifications for an Ad Hoc Command](op-api-v2-ad_hoc_commands-id-notifications-get.html)
:   Method: get

    Path: `/api/v2/ad_hoc_commands/{id}/notifications/`

[Relaunch an Ad Hoc Command](op-api-v2-ad_hoc_commands-id-relaunch-get.html)
:   Method: get

    Path: `/api/v2/ad_hoc_commands/{id}/relaunch/`

[Relaunch an Ad Hoc Command](op-api-v2-ad_hoc_commands-id-relaunch-post.html)
:   Method: post

    Path: `/api/v2/ad_hoc_commands/{id}/relaunch/`

[Retrieve Ad Hoc Command Stdout](op-api-v2-ad_hoc_commands-id-stdout-get.html)
:   Method: get

    Path: `/api/v2/ad_hoc_commands/{id}/stdout/`

[Retrieve an Ad Hoc Command](op-api-v2-ad_hoc_commands-id-get.html)
:   Method: get

    Path: `/api/v2/ad_hoc_commands/{id}/`

[Retrieve an Ad Hoc Command](op-api-v2-ad_hoc_commands-id-cancel-get.html)
:   Method: get

    Path: `/api/v2/ad_hoc_commands/{id}/cancel/`

[Retrieve an Ad Hoc Command](op-api-v2-ad_hoc_commands-id-cancel-post.html)
:   Method: post

    Path: `/api/v2/ad_hoc_commands/{id}/cancel/`


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-ad_hoc_commands-post.html -->

Make a POST request to this resource with the following ad hoc command
fields to create a new ad hoc command:

- `execution_environment`: The container image to be used for execution. (id, default=``)
- `job_type`: (choice)

  - `run`: Run (default)
  - `check`: Check
- `inventory`: (id, default=``)
- `limit`: (string, default=`""`)
- `credential`: (id, default=``)
- `module_name`: (choice)
  - `command` (default)
  - `shell`
  - `yum`
  - `apt`
  - `apt_key`
  - `apt_repository`
  - `apt_rpm`
  - `service`
  - `group`
  - `user`
  - `mount`
  - `ping`
  - `selinux`
  - `setup`
  - `win_ping`
  - `win_service`
  - `win_updates`
  - `win_group`
  - `win_user`
- `module_args`: (string, default=`""`)
- `forks`: (integer, default=`0`)
- `verbosity`: (choice)
  - `0`: 0 (Normal) (default)
  - `1`: 1 (Verbose)
  - `2`: 2 (More Verbose)
  - `3`: 3 (Debug)
  - `4`: 4 (Connection Debug)
  - `5`: 5 (WinRM Debug)
- `extra_vars`: (string, default=`""`)
- `become_enabled`: (boolean, default=`False`)
- `diff_mode`: (boolean, default=`False`)

### Request

Supported Media Types

- application/json

Body ()

Root Schema : AdHocCommandList

Type: `object`

[Show Source](#)

- [become\_enabled:
  boolean](#request-bodyparam-definitions-AdHocCommandList-properties-become_enabled-properties-become_enabled-0)

  Title: `Become enabled`
- [canceled\_on:
  string(date-time)](#request-bodyparam-definitions-AdHocCommandList-properties-canceled_on-properties-canceled_on-0)

  Title: `Canceled on`

  Read Only: `true`

  The date and time when the cancel request was sent.
- [controller\_node:
  string](#request-bodyparam-definitions-AdHocCommandList-properties-controller_node-properties-controller_node-0)

  Title: `Controller node`

  Read Only: `true`

  Minimum Length: `1`

  The instance that managed the execution environment.
- [created:
  string](#request-bodyparam-definitions-AdHocCommandList-properties-created-properties-created-0)

  Title: `Created`

  Read Only: `true`
- [credential:
  integer](#request-bodyparam-definitions-AdHocCommandList-properties-credential-properties-credential-0)

  Title: `Credential`
- [diff\_mode:
  boolean](#request-bodyparam-definitions-AdHocCommandList-properties-diff_mode-properties-diff_mode-0)

  Title: `Diff mode`
- [elapsed:
  string(decimal)](#request-bodyparam-definitions-AdHocCommandList-properties-elapsed-properties-elapsed-0)

  Title: `Elapsed`

  Read Only: `true`

  Elapsed time in seconds that the job ran.
- [execution\_environment:
  integer](#request-bodyparam-definitions-AdHocCommandList-properties-execution_environment-properties-execution_environment-0)

  Title: `Execution environment`

  The container image to be used for execution.
- [execution\_node:
  string](#request-bodyparam-definitions-AdHocCommandList-properties-execution_node-properties-execution_node-0)

  Title: `Execution node`

  Read Only: `true`

  Minimum Length: `1`

  The node the job executed on.
- [extra\_vars:
  string](#request-bodyparam-definitions-AdHocCommandList-properties-extra_vars-properties-extra_vars-0)

  Title: `Extra vars`
- [failed:
  boolean](#request-bodyparam-definitions-AdHocCommandList-properties-failed-properties-failed-0)

  Title: `Failed`

  Read Only: `true`
- [finished:
  string(date-time)](#request-bodyparam-definitions-AdHocCommandList-properties-finished-properties-finished-0)

  Title: `Finished`

  Read Only: `true`

  The date and time the job finished execution.
- [forks:
  integer](#request-bodyparam-definitions-AdHocCommandList-properties-forks-properties-forks-0)

  Title: `Forks`

  Minimum Value: `0`
- [id:
  integer](#request-bodyparam-definitions-AdHocCommandList-properties-id-properties-id-0)

  Title: `ID`

  Read Only: `true`
- [inventory:
  integer](#request-bodyparam-definitions-AdHocCommandList-properties-inventory-properties-inventory-0)

  Title: `Inventory`
- [job\_explanation:
  string](#request-bodyparam-definitions-AdHocCommandList-properties-job_explanation-properties-job_explanation-0)

  Title: `Job explanation`

  Read Only: `true`

  Minimum Length: `1`

  A status field to indicate the state of the job if it wasn't able to run and capture stdout
- [job\_type:
  string](#request-bodyparam-definitions-AdHocCommandList-properties-job_type-properties-job_type-0)

  Title: `Job type`

  Default Value: `run`

  Allowed Values: `[
  "run",
  "check"
  ]`
- [launch\_type:
  string](#request-bodyparam-definitions-AdHocCommandList-properties-launch_type-properties-launch_type-0)

  Title: `Launch type`

  Read Only: `true`

  Allowed Values: `[
  "manual",
  "relaunch",
  "callback",
  "scheduled",
  "dependency",
  "workflow",
  "webhook",
  "sync",
  "scm"
  ]`
- [launched\_by:
  string](#request-bodyparam-definitions-AdHocCommandList-properties-launched_by-properties-launched_by-0)

  Title: `Launched by`

  Read Only: `true`
- [limit:
  string](#request-bodyparam-definitions-AdHocCommandList-properties-limit-properties-limit-0)

  Title: `Limit`
- [modified:
  string](#request-bodyparam-definitions-AdHocCommandList-properties-modified-properties-modified-0)

  Title: `Modified`

  Read Only: `true`
- [module\_args:
  string](#request-bodyparam-definitions-AdHocCommandList-properties-module_args-properties-module_args-0)

  Title: `Module args`
- [module\_name:
  string](#request-bodyparam-definitions-AdHocCommandList-properties-module_name-properties-module_name-0)

  Title: `Module name`

  Default Value: `command`

  Allowed Values: `[
  "command",
  "shell",
  "yum",
  "apt",
  "apt_key",
  "apt_repository",
  "apt_rpm",
  "service",
  "group",
  "user",
  "mount",
  "ping",
  "selinux",
  "setup",
  "win_ping",
  "win_service",
  "win_updates",
  "win_group",
  "win_user"
  ]`
- [name:
  string](#request-bodyparam-definitions-AdHocCommandList-properties-name-properties-name-0)

  Title: `Name`

  Read Only: `true`

  Minimum Length: `1`
- [related:
  string](#request-bodyparam-definitions-AdHocCommandList-properties-related-properties-related-0)

  Title: `Related`

  Read Only: `true`
- [started:
  string(date-time)](#request-bodyparam-definitions-AdHocCommandList-properties-started-properties-started-0)

  Title: `Started`

  Read Only: `true`

  The date and time the job was queued for starting.
- [status:
  string](#request-bodyparam-definitions-AdHocCommandList-properties-status-properties-status-0)

  Title: `Status`

  Read Only: `true`

  Allowed Values: `[
  "new",
  "pending",
  "waiting",
  "running",
  "successful",
  "failed",
  "error",
  "canceled"
  ]`
- [summary\_fields:
  string](#request-bodyparam-definitions-AdHocCommandList-properties-summary_fields-properties-summary_fields-0)

  Title: `Summary fields`

  Read Only: `true`
- [type:
  string](#request-bodyparam-definitions-AdHocCommandList-properties-type-properties-type-0)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#request-bodyparam-definitions-AdHocCommandList-properties-url-properties-url-0)

  Title: `Url`

  Read Only: `true`
- [verbosity:
  integer](#request-bodyparam-definitions-AdHocCommandList-properties-verbosity-properties-verbosity-0)

  Title: `Verbosity`

  Allowed Values: `[
  "0",
  "1",
  "2",
  "3",
  "4",
  "5"
  ]`
- [work\_unit\_id:
  string](#request-bodyparam-definitions-AdHocCommandList-properties-work_unit_id-properties-work_unit_id-0)

  Title: `Work unit id`

  Read Only: `true`

  Minimum Length: `1`

  The Receptor work unit ID associated with this job.

```
{
    "properties":{
        "become_enabled":{
            "title":"Become enabled",
            "type":"boolean",
            "x-nullable":true
        },
        "canceled_on":{
            "description":"The date and time when the cancel request was sent.",
            "format":"date-time",
            "readOnly":true,
            "title":"Canceled on",
            "type":"string",
            "x-nullable":true
        },
        "controller_node":{
            "description":"The instance that managed the execution environment.",
            "minLength":"1",
            "readOnly":true,
            "title":"Controller node",
            "type":"string"
        },
        "created":{
            "readOnly":true,
            "title":"Created",
            "type":"string"
        },
        "credential":{
            "title":"Credential",
            "type":"integer",
            "x-nullable":true
        },
        "diff_mode":{
            "title":"Diff mode",
            "type":"boolean",
            "x-nullable":true
        },
        "elapsed":{
            "description":"Elapsed time in seconds that the job ran.",
            "format":"decimal",
            "readOnly":true,
            "title":"Elapsed",
            "type":"string"
        },
        "execution_environment":{
            "description":"The container image to be used for execution.",
            "title":"Execution environment",
            "type":"integer",
            "x-nullable":true
        },
        "execution_node":{
            "description":"The node the job executed on.",
            "minLength":"1",
            "readOnly":true,
            "title":"Execution node",
            "type":"string"
        },
        "extra_vars":{
            "title":"Extra vars",
            "type":"string",
            "x-nullable":true
        },
        "failed":{
            "readOnly":true,
            "title":"Failed",
            "type":"boolean"
        },
        "finished":{
            "description":"The date and time the job finished execution.",
            "format":"date-time",
            "readOnly":true,
            "title":"Finished",
            "type":"string",
            "x-nullable":true
        },
        "forks":{
            "minimum":"0",
            "title":"Forks",
            "type":"integer"
        },
        "id":{
            "readOnly":true,
            "title":"ID",
            "type":"integer"
        },
        "inventory":{
            "title":"Inventory",
            "type":"integer",
            "x-nullable":true
        },
        "job_explanation":{
            "description":"A status field to indicate the state of the job if it wasn't able to run and capture stdout",
            "minLength":"1",
            "readOnly":true,
            "title":"Job explanation",
            "type":"string"
        },
        "job_type":{
            "default":"run",
            "enum":[
                "run",
                "check"
            ],
            "title":"Job type",
            "type":"string",
            "x-nullable":true
        },
        "launch_type":{
            "enum":[
                "manual",
                "relaunch",
                "callback",
                "scheduled",
                "dependency",
                "workflow",
                "webhook",
                "sync",
                "scm"
            ],
            "readOnly":true,
            "title":"Launch type",
            "type":"string"
        },
        "launched_by":{
            "readOnly":true,
            "title":"Launched by",
            "type":"string"
        },
        "limit":{
            "title":"Limit",
            "type":"string",
            "x-nullable":true
        },
        "modified":{
            "readOnly":true,
            "title":"Modified",
            "type":"string"
        },
        "module_args":{
            "title":"Module args",
            "type":"string",
            "x-nullable":true
        },
        "module_name":{
            "default":"command",
            "enum":[
                "command",
                "shell",
                "yum",
                "apt",
                "apt_key",
                "apt_repository",
                "apt_rpm",
                "service",
                "group",
                "user",
                "mount",
                "ping",
                "selinux",
                "setup",
                "win_ping",
                "win_service",
                "win_updates",
                "win_group",
                "win_user"
            ],
            "title":"Module name",
            "type":"string"
        },
        "name":{
            "minLength":"1",
            "readOnly":true,
            "title":"Name",
            "type":"string",
            "x-nullable":true
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "started":{
            "description":"The date and time the job was queued for starting.",
            "format":"date-time",
            "readOnly":true,
            "title":"Started",
            "type":"string",
            "x-nullable":true
        },
        "status":{
            "enum":[
                "new",
                "pending",
                "waiting",
                "running",
                "successful",
                "failed",
                "error",
                "canceled"
            ],
            "readOnly":true,
            "title":"Status",
            "type":"string"
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        },
        "verbosity":{
            "enum":[
                "0",
                "1",
                "2",
                "3",
                "4",
                "5"
            ],
            "title":"Verbosity",
            "type":"integer"
        },
        "work_unit_id":{
            "description":"The Receptor work unit ID associated with this job.",
            "minLength":"1",
            "readOnly":true,
            "title":"Work unit id",
            "type":"string",
            "x-nullable":true
        }
    },
    "type":"object"
}
```

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

Body ()

Root Schema : AdHocCommandList

Type: `object`

[Show Source](#)

- [become\_enabled:
  boolean](#201-definitions-AdHocCommandList-properties-become_enabled-properties-become_enabled-0)

  Title: `Become enabled`
- [canceled\_on:
  string(date-time)](#201-definitions-AdHocCommandList-properties-canceled_on-properties-canceled_on-0)

  Title: `Canceled on`

  Read Only: `true`

  The date and time when the cancel request was sent.
- [controller\_node:
  string](#201-definitions-AdHocCommandList-properties-controller_node-properties-controller_node-0)

  Title: `Controller node`

  Read Only: `true`

  Minimum Length: `1`

  The instance that managed the execution environment.
- [created:
  string](#201-definitions-AdHocCommandList-properties-created-properties-created-0)

  Title: `Created`

  Read Only: `true`
- [credential:
  integer](#201-definitions-AdHocCommandList-properties-credential-properties-credential-0)

  Title: `Credential`
- [diff\_mode:
  boolean](#201-definitions-AdHocCommandList-properties-diff_mode-properties-diff_mode-0)

  Title: `Diff mode`
- [elapsed:
  string(decimal)](#201-definitions-AdHocCommandList-properties-elapsed-properties-elapsed-0)

  Title: `Elapsed`

  Read Only: `true`

  Elapsed time in seconds that the job ran.
- [execution\_environment:
  integer](#201-definitions-AdHocCommandList-properties-execution_environment-properties-execution_environment-0)

  Title: `Execution environment`

  The container image to be used for execution.
- [execution\_node:
  string](#201-definitions-AdHocCommandList-properties-execution_node-properties-execution_node-0)

  Title: `Execution node`

  Read Only: `true`

  Minimum Length: `1`

  The node the job executed on.
- [extra\_vars:
  string](#201-definitions-AdHocCommandList-properties-extra_vars-properties-extra_vars-0)

  Title: `Extra vars`
- [failed:
  boolean](#201-definitions-AdHocCommandList-properties-failed-properties-failed-0)

  Title: `Failed`

  Read Only: `true`
- [finished:
  string(date-time)](#201-definitions-AdHocCommandList-properties-finished-properties-finished-0)

  Title: `Finished`

  Read Only: `true`

  The date and time the job finished execution.
- [forks:
  integer](#201-definitions-AdHocCommandList-properties-forks-properties-forks-0)

  Title: `Forks`

  Minimum Value: `0`
- [id:
  integer](#201-definitions-AdHocCommandList-properties-id-properties-id-0)

  Title: `ID`

  Read Only: `true`
- [inventory:
  integer](#201-definitions-AdHocCommandList-properties-inventory-properties-inventory-0)

  Title: `Inventory`
- [job\_explanation:
  string](#201-definitions-AdHocCommandList-properties-job_explanation-properties-job_explanation-0)

  Title: `Job explanation`

  Read Only: `true`

  Minimum Length: `1`

  A status field to indicate the state of the job if it wasn't able to run and capture stdout
- [job\_type:
  string](#201-definitions-AdHocCommandList-properties-job_type-properties-job_type-0)

  Title: `Job type`

  Default Value: `run`

  Allowed Values: `[
  "run",
  "check"
  ]`
- [launch\_type:
  string](#201-definitions-AdHocCommandList-properties-launch_type-properties-launch_type-0)

  Title: `Launch type`

  Read Only: `true`

  Allowed Values: `[
  "manual",
  "relaunch",
  "callback",
  "scheduled",
  "dependency",
  "workflow",
  "webhook",
  "sync",
  "scm"
  ]`
- [launched\_by:
  string](#201-definitions-AdHocCommandList-properties-launched_by-properties-launched_by-0)

  Title: `Launched by`

  Read Only: `true`
- [limit:
  string](#201-definitions-AdHocCommandList-properties-limit-properties-limit-0)

  Title: `Limit`
- [modified:
  string](#201-definitions-AdHocCommandList-properties-modified-properties-modified-0)

  Title: `Modified`

  Read Only: `true`
- [module\_args:
  string](#201-definitions-AdHocCommandList-properties-module_args-properties-module_args-0)

  Title: `Module args`
- [module\_name:
  string](#201-definitions-AdHocCommandList-properties-module_name-properties-module_name-0)

  Title: `Module name`

  Default Value: `command`

  Allowed Values: `[
  "command",
  "shell",
  "yum",
  "apt",
  "apt_key",
  "apt_repository",
  "apt_rpm",
  "service",
  "group",
  "user",
  "mount",
  "ping",
  "selinux",
  "setup",
  "win_ping",
  "win_service",
  "win_updates",
  "win_group",
  "win_user"
  ]`
- [name:
  string](#201-definitions-AdHocCommandList-properties-name-properties-name-0)

  Title: `Name`

  Read Only: `true`

  Minimum Length: `1`
- [related:
  string](#201-definitions-AdHocCommandList-properties-related-properties-related-0)

  Title: `Related`

  Read Only: `true`
- [started:
  string(date-time)](#201-definitions-AdHocCommandList-properties-started-properties-started-0)

  Title: `Started`

  Read Only: `true`

  The date and time the job was queued for starting.
- [status:
  string](#201-definitions-AdHocCommandList-properties-status-properties-status-0)

  Title: `Status`

  Read Only: `true`

  Allowed Values: `[
  "new",
  "pending",
  "waiting",
  "running",
  "successful",
  "failed",
  "error",
  "canceled"
  ]`
- [summary\_fields:
  string](#201-definitions-AdHocCommandList-properties-summary_fields-properties-summary_fields-0)

  Title: `Summary fields`

  Read Only: `true`
- [type:
  string](#201-definitions-AdHocCommandList-properties-type-properties-type-0)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#201-definitions-AdHocCommandList-properties-url-properties-url-0)

  Title: `Url`

  Read Only: `true`
- [verbosity:
  integer](#201-definitions-AdHocCommandList-properties-verbosity-properties-verbosity-0)

  Title: `Verbosity`

  Allowed Values: `[
  "0",
  "1",
  "2",
  "3",
  "4",
  "5"
  ]`
- [work\_unit\_id:
  string](#201-definitions-AdHocCommandList-properties-work_unit_id-properties-work_unit_id-0)

  Title: `Work unit id`

  Read Only: `true`

  Minimum Length: `1`

  The Receptor work unit ID associated with this job.

```
{
    "properties":{
        "become_enabled":{
            "title":"Become enabled",
            "type":"boolean",
            "x-nullable":true
        },
        "canceled_on":{
            "description":"The date and time when the cancel request was sent.",
            "format":"date-time",
            "readOnly":true,
            "title":"Canceled on",
            "type":"string",
            "x-nullable":true
        },
        "controller_node":{
            "description":"The instance that managed the execution environment.",
            "minLength":"1",
            "readOnly":true,
            "title":"Controller node",
            "type":"string"
        },
        "created":{
            "readOnly":true,
            "title":"Created",
            "type":"string"
        },
        "credential":{
            "title":"Credential",
            "type":"integer",
            "x-nullable":true
        },
        "diff_mode":{
            "title":"Diff mode",
            "type":"boolean",
            "x-nullable":true
        },
        "elapsed":{
            "description":"Elapsed time in seconds that the job ran.",
            "format":"decimal",
            "readOnly":true,
            "title":"Elapsed",
            "type":"string"
        },
        "execution_environment":{
            "description":"The container image to be used for execution.",
            "title":"Execution environment",
            "type":"integer",
            "x-nullable":true
        },
        "execution_node":{
            "description":"The node the job executed on.",
            "minLength":"1",
            "readOnly":true,
            "title":"Execution node",
            "type":"string"
        },
        "extra_vars":{
            "title":"Extra vars",
            "type":"string",
            "x-nullable":true
        },
        "failed":{
            "readOnly":true,
            "title":"Failed",
            "type":"boolean"
        },
        "finished":{
            "description":"The date and time the job finished execution.",
            "format":"date-time",
            "readOnly":true,
            "title":"Finished",
            "type":"string",
            "x-nullable":true
        },
        "forks":{
            "minimum":"0",
            "title":"Forks",
            "type":"integer"
        },
        "id":{
            "readOnly":true,
            "title":"ID",
            "type":"integer"
        },
        "inventory":{
            "title":"Inventory",
            "type":"integer",
            "x-nullable":true
        },
        "job_explanation":{
            "description":"A status field to indicate the state of the job if it wasn't able to run and capture stdout",
            "minLength":"1",
            "readOnly":true,
            "title":"Job explanation",
            "type":"string"
        },
        "job_type":{
            "default":"run",
            "enum":[
                "run",
                "check"
            ],
            "title":"Job type",
            "type":"string",
            "x-nullable":true
        },
        "launch_type":{
            "enum":[
                "manual",
                "relaunch",
                "callback",
                "scheduled",
                "dependency",
                "workflow",
                "webhook",
                "sync",
                "scm"
            ],
            "readOnly":true,
            "title":"Launch type",
            "type":"string"
        },
        "launched_by":{
            "readOnly":true,
            "title":"Launched by",
            "type":"string"
        },
        "limit":{
            "title":"Limit",
            "type":"string",
            "x-nullable":true
        },
        "modified":{
            "readOnly":true,
            "title":"Modified",
            "type":"string"
        },
        "module_args":{
            "title":"Module args",
            "type":"string",
            "x-nullable":true
        },
        "module_name":{
            "default":"command",
            "enum":[
                "command",
                "shell",
                "yum",
                "apt",
                "apt_key",
                "apt_repository",
                "apt_rpm",
                "service",
                "group",
                "user",
                "mount",
                "ping",
                "selinux",
                "setup",
                "win_ping",
                "win_service",
                "win_updates",
                "win_group",
                "win_user"
            ],
            "title":"Module name",
            "type":"string"
        },
        "name":{
            "minLength":"1",
            "readOnly":true,
            "title":"Name",
            "type":"string",
            "x-nullable":true
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "started":{
            "description":"The date and time the job was queued for starting.",
            "format":"date-time",
            "readOnly":true,
            "title":"Started",
            "type":"string",
            "x-nullable":true
        },
        "status":{
            "enum":[
                "new",
                "pending",
                "waiting",
                "running",
                "successful",
                "failed",
                "error",
                "canceled"
            ],
            "readOnly":true,
            "title":"Status",
            "type":"string"
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        },
        "verbosity":{
            "enum":[
                "0",
                "1",
                "2",
                "3",
                "4",
                "5"
            ],
            "title":"Verbosity",
            "type":"integer"
        },
        "work_unit_id":{
            "description":"The Receptor work unit ID associated with this job.",
            "minLength":"1",
            "readOnly":true,
            "title":"Work unit id",
            "type":"string",
            "x-nullable":true
        }
    },
    "type":"object"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-ad_hoc_commands-id-delete.html -->

Make a DELETE request to this resource to delete this ad hoc command.

### Request

Supported Media Types

- application/json

Path Parameters

- [id(required): string](#request-path-param-0)

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 204 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-ad_hoc_commands-id-activity_stream-get.html -->

Make a GET request to this resource to retrieve a list of
activity streams associated with the selected
ad hoc command.

The resulting data structure contains:

```
{
    "count": 99,
    "next": null,
    "previous": null,
    "results": [
        ...
    ]
}
```

The `count` field indicates the total number of activity streams
found for the given query. The `next` and `previous` fields provides links to
additional results if there are more than will fit on a single page. The
`results` list contains zero or more activity stream records.

## Results

Each activity stream data structure includes the following fields:

- `id`: Database ID for this activity stream. (integer)
- `type`: Data type for this activity stream. (choice)
- `url`: URL for this activity stream. (string)
- `related`: Data structure with URLs of related resources. (object)
- `summary_fields`: Data structure with name/description for related resources. The output for some objects may be limited for performance reasons. (object)
- `timestamp`: (datetime)
- `operation`: The action taken with respect to the given object(s). (choice)
  - `create`: Entity Created
  - `update`: Entity Updated
  - `delete`: Entity Deleted
  - `associate`: Entity Associated with another Entity
  - `disassociate`: Entity was Disassociated with another Entity
- `changes`: A summary of the new and changed values when an object is created, updated, or deleted (json)
- `object1`: For create, update, and delete events this is the object type that was affected. For associate and disassociate events this is the object type associated or disassociated with object2. (string)
- `object2`: Unpopulated for create, update, and delete events. For associate and disassociate events this is the object type that object1 is being associated with. (string)
- `object_association`: When present, shows the field name of the role or relationship that changed. (field)
- `action_node`: The cluster node the activity took place on. (string)
- `object_type`: When present, shows the model on which the role or relationship was defined. (field)

## Sorting

To specify that activity streams are returned in a particular
order, use the `order_by` query string parameter on the GET request.

```
?order_by=name
```

Prefix the field name with a dash `-` to sort in reverse:

```
?order_by=-name
```

Multiple sorting fields may be specified by separating the field names with a
comma `,`:

```
?order_by=name,some_other_field
```

## Pagination

Use the `page_size` query string parameter to change the number of results
returned for each request. Use the `page` query string parameter to retrieve
a particular page of results.

```
?page_size=100&page=2
```

The `previous` and `next` links returned with the results will set these query
string parameters automatically.

## Searching

Use the `search` query string parameter to perform a case-insensitive search
within all designated text fields of a model.

```
?search=findme
```

(*Added in Ansible Tower 3.1.0*) Search across related fields:

```
?related__search=findme
```

### Request

Supported Media Types

- application/json

Path Parameters

- [id(required): string](#request-path-param-0)

Query Parameters

- [page: integer](#request-query-param-0)

  A page number within the paginated result set.
- [page\_size: integer](#request-query-param-1)

  Number of results to return per page.
- [search: string](#request-query-param-2)

  A search term.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

Body ()

Root Schema : schema

Type: `object`

[Show Source](#)

- [count(required):
  integer](#200-paths--api-v2-ad_hoc_commands-{id}-activity_stream--get-responses-200-schema-properties-count-properties-count-0)
- [next:
  string(uri)](#200-paths--api-v2-ad_hoc_commands-{id}-activity_stream--get-responses-200-schema-properties-next-properties-next-0)
- [previous:
  string(uri)](#200-paths--api-v2-ad_hoc_commands-{id}-activity_stream--get-responses-200-schema-properties-previous-properties-previous-0)
- [results(required):
  array](#200-paths--api-v2-ad_hoc_commands-{id}-activity_stream--get-responses-200-schema-properties-results-properties-results-0)  [results](#200-paths--api-v2-ad_hoc_commands-{id}-activity_stream--get-responses-200-schema-properties-results)

```
{
    "properties":{
        "count":{
            "type":"integer"
        },
        "next":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "previous":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "results":{
            "items":{
                "$ref":"#/definitions/ActivityStream"
            },
            "type":"array"
        }
    },
    "required":[
        "count",
        "results"
    ],
    "type":"object"
}
```

Nested Schema : results

Type: `array`

[Show Source](#)

- [Array of:
  object](#200-definitions-ActivityStream-items-0)  [ActivityStream](#200-definitions-ActivityStream)

```
{
    "items":{
        "$ref":"#/definitions/ActivityStream"
    },
    "type":"array"
}
```

Nested Schema : ActivityStream

Type: `object`

[Show Source](#)

- [action\_node:
  string](#200-definitions-ActivityStream-properties-action_node-properties-action_node-2)

  Title: `Action node`

  Read Only: `true`

  Minimum Length: `1`

  The cluster node the activity took place on.
- [changes:
  string](#200-definitions-ActivityStream-properties-changes-properties-changes-2)

  Title: `Changes`

  Read Only: `true`

  A summary of the new and changed values when an object is created, updated, or deleted
- [id:
  integer](#200-definitions-ActivityStream-properties-id-properties-id-2)

  Title: `ID`

  Read Only: `true`
- [object1(required):
  string](#200-definitions-ActivityStream-properties-object1-properties-object1-2)

  Title: `Object1`

  Minimum Length: `1`

  For create, update, and delete events this is the object type that was affected. For associate and disassociate events this is the object type associated or disassociated with object2.
- [object2(required):
  string](#200-definitions-ActivityStream-properties-object2-properties-object2-2)

  Title: `Object2`

  Minimum Length: `1`

  Unpopulated for create, update, and delete events. For associate and disassociate events this is the object type that object1 is being associated with.
- [object\_association:
  string](#200-definitions-ActivityStream-properties-object_association-properties-object_association-2)

  Title: `Object association`

  Read Only: `true`

  When present, shows the field name of the role or relationship that changed.
- [object\_type:
  string](#200-definitions-ActivityStream-properties-object_type-properties-object_type-2)

  Title: `Object type`

  Read Only: `true`

  When present, shows the model on which the role or relationship was defined.
- [operation(required):
  string](#200-definitions-ActivityStream-properties-operation-properties-operation-2)

  Title: `Operation`

  Allowed Values: `[
  "create",
  "update",
  "delete",
  "associate",
  "disassociate"
  ]`

  The action taken with respect to the given object(s).
- [related:
  string](#200-definitions-ActivityStream-properties-related-properties-related-2)

  Title: `Related`

  Read Only: `true`
- [summary\_fields:
  string](#200-definitions-ActivityStream-properties-summary_fields-properties-summary_fields-2)

  Title: `Summary fields`

  Read Only: `true`
- [timestamp:
  string(date-time)](#200-definitions-ActivityStream-properties-timestamp-properties-timestamp-2)

  Title: `Timestamp`

  Read Only: `true`
- [type:
  string](#200-definitions-ActivityStream-properties-type-properties-type-2)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#200-definitions-ActivityStream-properties-url-properties-url-2)

  Title: `Url`

  Read Only: `true`

```
{
    "properties":{
        "action_node":{
            "description":"The cluster node the activity took place on.",
            "minLength":"1",
            "readOnly":true,
            "title":"Action node",
            "type":"string"
        },
        "changes":{
            "description":"A summary of the new and changed values when an object is created, updated, or deleted",
            "readOnly":true,
            "title":"Changes",
            "type":"string"
        },
        "id":{
            "readOnly":true,
            "title":"ID",
            "type":"integer"
        },
        "object1":{
            "description":"For create, update, and delete events this is the object type that was affected. For associate and disassociate events this is the object type associated or disassociated with object2.",
            "minLength":"1",
            "title":"Object1",
            "type":"string",
            "x-nullable":true
        },
        "object2":{
            "description":"Unpopulated for create, update, and delete events. For associate and disassociate events this is the object type that object1 is being associated with.",
            "minLength":"1",
            "title":"Object2",
            "type":"string",
            "x-nullable":true
        },
        "object_association":{
            "description":"When present, shows the field name of the role or relationship that changed.",
            "readOnly":true,
            "title":"Object association",
            "type":"string"
        },
        "object_type":{
            "description":"When present, shows the model on which the role or relationship was defined.",
            "readOnly":true,
            "title":"Object type",
            "type":"string"
        },
        "operation":{
            "description":"The action taken with respect to the given object(s).",
            "enum":[
                "create",
                "update",
                "delete",
                "associate",
                "disassociate"
            ],
            "title":"Operation",
            "type":"string",
            "x-nullable":true
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "timestamp":{
            "format":"date-time",
            "readOnly":true,
            "title":"Timestamp",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        }
    },
    "required":[
        "operation",
        "object1",
        "object2"
    ],
    "type":"object"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-ad_hoc_commands-id-events-get.html -->

Make a GET request to this resource to retrieve a list of
ad hoc command events associated with the selected
ad hoc command.

The resulting data structure contains:

```
{
    "count": 99,
    "next": null,
    "previous": null,
    "results": [
        ...
    ]
}
```

The `count` field indicates the total number of ad hoc command events
found for the given query. The `next` and `previous` fields provides links to
additional results if there are more than will fit on a single page. The
`results` list contains zero or more ad hoc command event records.

## Results

Each ad hoc command event data structure includes the following fields:

- `id`: Database ID for this ad hoc command event. (integer)
- `type`: Data type for this ad hoc command event. (choice)
- `url`: URL for this ad hoc command event. (string)
- `related`: Data structure with URLs of related resources. (object)
- `summary_fields`: Data structure with name/description for related resources. The output for some objects may be limited for performance reasons. (object)
- `created`: Timestamp when this ad hoc command event was created. (datetime)
- `modified`: Timestamp when this ad hoc command event was last modified. (datetime)
- `ad_hoc_command`: (id)
- `event`: (choice)
  - `runner_on_failed`: Host Failed
  - `runner_on_ok`: Host OK
  - `runner_on_unreachable`: Host Unreachable
  - `runner_on_skipped`: Host Skipped
  - `debug`: Debug
  - `verbose`: Verbose
  - `deprecated`: Deprecated
  - `warning`: Warning
  - `system_warning`: System Warning
  - `error`: Error
- `counter`: (integer)
- `event_display`: (string)
- `event_data`: (json)
- `failed`: (boolean)
- `changed`: (boolean)
- `uuid`: (string)
- `host`: (id)
- `host_name`: (string)
- `stdout`: (string)
- `start_line`: (integer)
- `end_line`: (integer)
- `verbosity`: (integer)

## Sorting

To specify that ad hoc command events are returned in a particular
order, use the `order_by` query string parameter on the GET request.

```
?order_by=name
```

Prefix the field name with a dash `-` to sort in reverse:

```
?order_by=-name
```

Multiple sorting fields may be specified by separating the field names with a
comma `,`:

```
?order_by=name,some_other_field
```

## Pagination

Use the `page_size` query string parameter to change the number of results
returned for each request. Use the `page` query string parameter to retrieve
a particular page of results.

```
?page_size=100&page=2
```

The `previous` and `next` links returned with the results will set these query
string parameters automatically.

## Searching

Use the `search` query string parameter to perform a case-insensitive search
within all designated text fields of a model.

```
?search=findme
```

(*Added in Ansible Tower 3.1.0*) Search across related fields:

```
?related__search=findme
```

### Request

Supported Media Types

- application/json

Path Parameters

- [id(required): string](#request-path-param-0)

Query Parameters

- [page: integer](#request-query-param-0)

  A page number within the paginated result set.
- [page\_size: integer](#request-query-param-1)

  Number of results to return per page.
- [search: string](#request-query-param-2)

  A search term.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

Body ()

Root Schema : schema

Type: `object`

[Show Source](#)

- [count(required):
  integer](#200-paths--api-v2-ad_hoc_commands-{id}-events--get-responses-200-schema-properties-count-properties-count-0)
- [next:
  string(uri)](#200-paths--api-v2-ad_hoc_commands-{id}-events--get-responses-200-schema-properties-next-properties-next-0)
- [previous:
  string(uri)](#200-paths--api-v2-ad_hoc_commands-{id}-events--get-responses-200-schema-properties-previous-properties-previous-0)
- [results(required):
  array](#200-paths--api-v2-ad_hoc_commands-{id}-events--get-responses-200-schema-properties-results-properties-results-0)  [results](#200-paths--api-v2-ad_hoc_commands-{id}-events--get-responses-200-schema-properties-results)

```
{
    "properties":{
        "count":{
            "type":"integer"
        },
        "next":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "previous":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "results":{
            "items":{
                "$ref":"#/definitions/AdHocCommandEvent"
            },
            "type":"array"
        }
    },
    "required":[
        "count",
        "results"
    ],
    "type":"object"
}
```

Nested Schema : results

Type: `array`

[Show Source](#)

- [Array of:
  object](#200-definitions-AdHocCommandEvent-items-0)  [AdHocCommandEvent](#200-definitions-AdHocCommandEvent)

```
{
    "items":{
        "$ref":"#/definitions/AdHocCommandEvent"
    },
    "type":"array"
}
```

Nested Schema : AdHocCommandEvent

Type: `object`

[Show Source](#)

- [ad\_hoc\_command:
  string](#200-definitions-AdHocCommandEvent-properties-ad_hoc_command-properties-ad_hoc_command-1)

  Title: `Ad hoc command`

  Read Only: `true`
- [changed:
  boolean](#200-definitions-AdHocCommandEvent-properties-changed-properties-changed-1)

  Title: `Changed`

  Read Only: `true`
- [counter:
  integer](#200-definitions-AdHocCommandEvent-properties-counter-properties-counter-1)

  Title: `Counter`

  Read Only: `true`

  Minimum Value: `0`
- [created:
  string](#200-definitions-AdHocCommandEvent-properties-created-properties-created-1)

  Title: `Created`

  Read Only: `true`
- [end\_line:
  integer](#200-definitions-AdHocCommandEvent-properties-end_line-properties-end_line-1)

  Title: `End line`

  Read Only: `true`

  Minimum Value: `0`
- [event(required):
  string](#200-definitions-AdHocCommandEvent-properties-event-properties-event-1)

  Title: `Event`

  Allowed Values: `[
  "runner_on_failed",
  "runner_on_ok",
  "runner_on_unreachable",
  "runner_on_skipped",
  "debug",
  "verbose",
  "deprecated",
  "warning",
  "system_warning",
  "error"
  ]`
- [event\_data:
  object](#200-definitions-AdHocCommandEvent-properties-event_data-properties-event_data-1)  [Event data](#200-definitions-AdHocCommandEvent-properties-event_data)

  Title: `Event data`
- [event\_display:
  string](#200-definitions-AdHocCommandEvent-properties-event_display-properties-event_display-1)

  Title: `Event display`

  Read Only: `true`

  Minimum Length: `1`
- [failed:
  boolean](#200-definitions-AdHocCommandEvent-properties-failed-properties-failed-1)

  Title: `Failed`

  Read Only: `true`
- [host:
  integer](#200-definitions-AdHocCommandEvent-properties-host-properties-host-1)

  Title: `Host`

  Read Only: `true`
- [host\_name:
  string](#200-definitions-AdHocCommandEvent-properties-host_name-properties-host_name-1)

  Title: `Host name`

  Read Only: `true`

  Minimum Length: `1`
- [id:
  integer](#200-definitions-AdHocCommandEvent-properties-id-properties-id-1)

  Title: `ID`

  Read Only: `true`
- [modified:
  string](#200-definitions-AdHocCommandEvent-properties-modified-properties-modified-1)

  Title: `Modified`

  Read Only: `true`
- [related:
  string](#200-definitions-AdHocCommandEvent-properties-related-properties-related-1)

  Title: `Related`

  Read Only: `true`
- [start\_line:
  integer](#200-definitions-AdHocCommandEvent-properties-start_line-properties-start_line-1)

  Title: `Start line`

  Read Only: `true`

  Minimum Value: `0`
- [stdout:
  string](#200-definitions-AdHocCommandEvent-properties-stdout-properties-stdout-1)

  Title: `Stdout`

  Read Only: `true`

  Minimum Length: `1`
- [summary\_fields:
  string](#200-definitions-AdHocCommandEvent-properties-summary_fields-properties-summary_fields-1)

  Title: `Summary fields`

  Read Only: `true`
- [type:
  string](#200-definitions-AdHocCommandEvent-properties-type-properties-type-1)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#200-definitions-AdHocCommandEvent-properties-url-properties-url-1)

  Title: `Url`

  Read Only: `true`
- [uuid:
  string](#200-definitions-AdHocCommandEvent-properties-uuid-properties-uuid-1)

  Title: `Uuid`

  Read Only: `true`

  Minimum Length: `1`
- [verbosity:
  integer](#200-definitions-AdHocCommandEvent-properties-verbosity-properties-verbosity-1)

  Title: `Verbosity`

  Read Only: `true`

  Minimum Value: `0`

```
{
    "properties":{
        "ad_hoc_command":{
            "readOnly":true,
            "title":"Ad hoc command",
            "type":"string"
        },
        "changed":{
            "readOnly":true,
            "title":"Changed",
            "type":"boolean"
        },
        "counter":{
            "minimum":"0",
            "readOnly":true,
            "title":"Counter",
            "type":"integer"
        },
        "created":{
            "readOnly":true,
            "title":"Created",
            "type":"string"
        },
        "end_line":{
            "minimum":"0",
            "readOnly":true,
            "title":"End line",
            "type":"integer"
        },
        "event":{
            "enum":[
                "runner_on_failed",
                "runner_on_ok",
                "runner_on_unreachable",
                "runner_on_skipped",
                "debug",
                "verbose",
                "deprecated",
                "warning",
                "system_warning",
                "error"
            ],
            "title":"Event",
            "type":"string",
            "x-nullable":true
        },
        "event_data":{
            "title":"Event data",
            "type":"object"
        },
        "event_display":{
            "minLength":"1",
            "readOnly":true,
            "title":"Event display",
            "type":"string"
        },
        "failed":{
            "readOnly":true,
            "title":"Failed",
            "type":"boolean"
        },
        "host":{
            "readOnly":true,
            "title":"Host",
            "type":"integer",
            "x-nullable":true
        },
        "host_name":{
            "minLength":"1",
            "readOnly":true,
            "title":"Host name",
            "type":"string"
        },
        "id":{
            "readOnly":true,
            "title":"ID",
            "type":"integer"
        },
        "modified":{
            "readOnly":true,
            "title":"Modified",
            "type":"string"
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "start_line":{
            "minimum":"0",
            "readOnly":true,
            "title":"Start line",
            "type":"integer"
        },
        "stdout":{
            "minLength":"1",
            "readOnly":true,
            "title":"Stdout",
            "type":"string"
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        },
        "uuid":{
            "minLength":"1",
            "readOnly":true,
            "title":"Uuid",
            "type":"string"
        },
        "verbosity":{
            "minimum":"0",
            "readOnly":true,
            "title":"Verbosity",
            "type":"integer"
        }
    },
    "required":[
        "event"
    ],
    "type":"object"
}
```

Nested Schema : Event data

Type: `object`

Title: `Event data`

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-ad_hoc_commands-get.html -->

Make a GET request to this resource to retrieve the list of
ad hoc commands.

The resulting data structure contains:

```
{
    "count": 99,
    "next": null,
    "previous": null,
    "results": [
        ...
    ]
}
```

The `count` field indicates the total number of ad hoc commands
found for the given query. The `next` and `previous` fields provides links to
additional results if there are more than will fit on a single page. The
`results` list contains zero or more ad hoc command records.

## Results

Each ad hoc command data structure includes the following fields:

- `id`: Database ID for this ad hoc command. (integer)
- `type`: Data type for this ad hoc command. (choice)
- `url`: URL for this ad hoc command. (string)
- `related`: Data structure with URLs of related resources. (object)
- `summary_fields`: Data structure with name/description for related resources. The output for some objects may be limited for performance reasons. (object)
- `created`: Timestamp when this ad hoc command was created. (datetime)
- `modified`: Timestamp when this ad hoc command was last modified. (datetime)
- `name`: Name of this ad hoc command. (string)
- `launch_type`: (choice)
  - `manual`: Manual
  - `relaunch`: Relaunch
  - `callback`: Callback
  - `scheduled`: Scheduled
  - `dependency`: Dependency
  - `workflow`: Workflow
  - `webhook`: Webhook
  - `sync`: Sync
  - `scm`: SCM Update
- `status`: (choice)
  - `new`: New
  - `pending`: Pending
  - `waiting`: Waiting
  - `running`: Running
  - `successful`: Successful
  - `failed`: Failed
  - `error`: Error
  - `canceled`: Canceled
- `execution_environment`: The container image to be used for execution. (id)
- `failed`: (boolean)
- `started`: The date and time the job was queued for starting. (datetime)
- `finished`: The date and time the job finished execution. (datetime)
- `canceled_on`: The date and time when the cancel request was sent. (datetime)
- `elapsed`: Elapsed time in seconds that the job ran. (decimal)
- `job_explanation`: A status field to indicate the state of the job if it wasn't able to run and capture stdout (string)
- `execution_node`: The node the job executed on. (string)
- `controller_node`: The instance that managed the execution environment. (string)
- `launched_by`: (field)
- `work_unit_id`: The Receptor work unit ID associated with this job. (string)
- `job_type`: (choice)
  - `run`: Run
  - `check`: Check
- `inventory`: (id)
- `limit`: (string)
- `credential`: (id)
- `module_name`: (choice)
  - `command`
  - `shell`
  - `yum`
  - `apt`
  - `apt_key`
  - `apt_repository`
  - `apt_rpm`
  - `service`
  - `group`
  - `user`
  - `mount`
  - `ping`
  - `selinux`
  - `setup`
  - `win_ping`
  - `win_service`
  - `win_updates`
  - `win_group`
  - `win_user`
- `module_args`: (string)
- `forks`: (integer)
- `verbosity`: (choice)
  - `0`: 0 (Normal)
  - `1`: 1 (Verbose)
  - `2`: 2 (More Verbose)
  - `3`: 3 (Debug)
  - `4`: 4 (Connection Debug)
  - `5`: 5 (WinRM Debug)
- `extra_vars`: (string)
- `become_enabled`: (boolean)
- `diff_mode`: (boolean)

## Sorting

To specify that ad hoc commands are returned in a particular
order, use the `order_by` query string parameter on the GET request.

```
?order_by=name
```

Prefix the field name with a dash `-` to sort in reverse:

```
?order_by=-name
```

Multiple sorting fields may be specified by separating the field names with a
comma `,`:

```
?order_by=name,some_other_field
```

## Pagination

Use the `page_size` query string parameter to change the number of results
returned for each request. Use the `page` query string parameter to retrieve
a particular page of results.

```
?page_size=100&page=2
```

The `previous` and `next` links returned with the results will set these query
string parameters automatically.

## Searching

Use the `search` query string parameter to perform a case-insensitive search
within all designated text fields of a model.

```
?search=findme
```

(*Added in Ansible Tower 3.1.0*) Search across related fields:

```
?related__search=findme
```

### Request

Supported Media Types

- application/json

Query Parameters

- [page: integer](#request-query-param-0)

  A page number within the paginated result set.
- [page\_size: integer](#request-query-param-1)

  Number of results to return per page.
- [search: string](#request-query-param-2)

  A search term.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

Body ()

Root Schema : schema

Type: `object`

[Show Source](#)

- [count(required):
  integer](#200-paths--api-v2-ad_hoc_commands--get-responses-200-schema-properties-count-properties-count-0)
- [next:
  string(uri)](#200-paths--api-v2-ad_hoc_commands--get-responses-200-schema-properties-next-properties-next-0)
- [previous:
  string(uri)](#200-paths--api-v2-ad_hoc_commands--get-responses-200-schema-properties-previous-properties-previous-0)
- [results(required):
  array](#200-paths--api-v2-ad_hoc_commands--get-responses-200-schema-properties-results-properties-results-0)  [results](#200-paths--api-v2-ad_hoc_commands--get-responses-200-schema-properties-results)

```
{
    "properties":{
        "count":{
            "type":"integer"
        },
        "next":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "previous":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "results":{
            "items":{
                "$ref":"#/definitions/AdHocCommandList"
            },
            "type":"array"
        }
    },
    "required":[
        "count",
        "results"
    ],
    "type":"object"
}
```

Nested Schema : results

Type: `array`

[Show Source](#)

- [Array of:
  object](#200-definitions-AdHocCommandList-items-0)  [AdHocCommandList](#200-definitions-AdHocCommandList)

```
{
    "items":{
        "$ref":"#/definitions/AdHocCommandList"
    },
    "type":"array"
}
```

Nested Schema : AdHocCommandList

Type: `object`

[Show Source](#)

- [become\_enabled:
  boolean](#200-definitions-AdHocCommandList-properties-become_enabled-properties-become_enabled-0)

  Title: `Become enabled`
- [canceled\_on:
  string(date-time)](#200-definitions-AdHocCommandList-properties-canceled_on-properties-canceled_on-0)

  Title: `Canceled on`

  Read Only: `true`

  The date and time when the cancel request was sent.
- [controller\_node:
  string](#200-definitions-AdHocCommandList-properties-controller_node-properties-controller_node-0)

  Title: `Controller node`

  Read Only: `true`

  Minimum Length: `1`

  The instance that managed the execution environment.
- [created:
  string](#200-definitions-AdHocCommandList-properties-created-properties-created-0)

  Title: `Created`

  Read Only: `true`
- [credential:
  integer](#200-definitions-AdHocCommandList-properties-credential-properties-credential-0)

  Title: `Credential`
- [diff\_mode:
  boolean](#200-definitions-AdHocCommandList-properties-diff_mode-properties-diff_mode-0)

  Title: `Diff mode`
- [elapsed:
  string(decimal)](#200-definitions-AdHocCommandList-properties-elapsed-properties-elapsed-0)

  Title: `Elapsed`

  Read Only: `true`

  Elapsed time in seconds that the job ran.
- [execution\_environment:
  integer](#200-definitions-AdHocCommandList-properties-execution_environment-properties-execution_environment-0)

  Title: `Execution environment`

  The container image to be used for execution.
- [execution\_node:
  string](#200-definitions-AdHocCommandList-properties-execution_node-properties-execution_node-0)

  Title: `Execution node`

  Read Only: `true`

  Minimum Length: `1`

  The node the job executed on.
- [extra\_vars:
  string](#200-definitions-AdHocCommandList-properties-extra_vars-properties-extra_vars-0)

  Title: `Extra vars`
- [failed:
  boolean](#200-definitions-AdHocCommandList-properties-failed-properties-failed-0)

  Title: `Failed`

  Read Only: `true`
- [finished:
  string(date-time)](#200-definitions-AdHocCommandList-properties-finished-properties-finished-0)

  Title: `Finished`

  Read Only: `true`

  The date and time the job finished execution.
- [forks:
  integer](#200-definitions-AdHocCommandList-properties-forks-properties-forks-0)

  Title: `Forks`

  Minimum Value: `0`
- [id:
  integer](#200-definitions-AdHocCommandList-properties-id-properties-id-0)

  Title: `ID`

  Read Only: `true`
- [inventory:
  integer](#200-definitions-AdHocCommandList-properties-inventory-properties-inventory-0)

  Title: `Inventory`
- [job\_explanation:
  string](#200-definitions-AdHocCommandList-properties-job_explanation-properties-job_explanation-0)

  Title: `Job explanation`

  Read Only: `true`

  Minimum Length: `1`

  A status field to indicate the state of the job if it wasn't able to run and capture stdout
- [job\_type:
  string](#200-definitions-AdHocCommandList-properties-job_type-properties-job_type-0)

  Title: `Job type`

  Default Value: `run`

  Allowed Values: `[
  "run",
  "check"
  ]`
- [launch\_type:
  string](#200-definitions-AdHocCommandList-properties-launch_type-properties-launch_type-0)

  Title: `Launch type`

  Read Only: `true`

  Allowed Values: `[
  "manual",
  "relaunch",
  "callback",
  "scheduled",
  "dependency",
  "workflow",
  "webhook",
  "sync",
  "scm"
  ]`
- [launched\_by:
  string](#200-definitions-AdHocCommandList-properties-launched_by-properties-launched_by-0)

  Title: `Launched by`

  Read Only: `true`
- [limit:
  string](#200-definitions-AdHocCommandList-properties-limit-properties-limit-0)

  Title: `Limit`
- [modified:
  string](#200-definitions-AdHocCommandList-properties-modified-properties-modified-0)

  Title: `Modified`

  Read Only: `true`
- [module\_args:
  string](#200-definitions-AdHocCommandList-properties-module_args-properties-module_args-0)

  Title: `Module args`
- [module\_name:
  string](#200-definitions-AdHocCommandList-properties-module_name-properties-module_name-0)

  Title: `Module name`

  Default Value: `command`

  Allowed Values: `[
  "command",
  "shell",
  "yum",
  "apt",
  "apt_key",
  "apt_repository",
  "apt_rpm",
  "service",
  "group",
  "user",
  "mount",
  "ping",
  "selinux",
  "setup",
  "win_ping",
  "win_service",
  "win_updates",
  "win_group",
  "win_user"
  ]`
- [name:
  string](#200-definitions-AdHocCommandList-properties-name-properties-name-0)

  Title: `Name`

  Read Only: `true`

  Minimum Length: `1`
- [related:
  string](#200-definitions-AdHocCommandList-properties-related-properties-related-0)

  Title: `Related`

  Read Only: `true`
- [started:
  string(date-time)](#200-definitions-AdHocCommandList-properties-started-properties-started-0)

  Title: `Started`

  Read Only: `true`

  The date and time the job was queued for starting.
- [status:
  string](#200-definitions-AdHocCommandList-properties-status-properties-status-0)

  Title: `Status`

  Read Only: `true`

  Allowed Values: `[
  "new",
  "pending",
  "waiting",
  "running",
  "successful",
  "failed",
  "error",
  "canceled"
  ]`
- [summary\_fields:
  string](#200-definitions-AdHocCommandList-properties-summary_fields-properties-summary_fields-0)

  Title: `Summary fields`

  Read Only: `true`
- [type:
  string](#200-definitions-AdHocCommandList-properties-type-properties-type-0)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#200-definitions-AdHocCommandList-properties-url-properties-url-0)

  Title: `Url`

  Read Only: `true`
- [verbosity:
  integer](#200-definitions-AdHocCommandList-properties-verbosity-properties-verbosity-0)

  Title: `Verbosity`

  Allowed Values: `[
  "0",
  "1",
  "2",
  "3",
  "4",
  "5"
  ]`
- [work\_unit\_id:
  string](#200-definitions-AdHocCommandList-properties-work_unit_id-properties-work_unit_id-0)

  Title: `Work unit id`

  Read Only: `true`

  Minimum Length: `1`

  The Receptor work unit ID associated with this job.

```
{
    "properties":{
        "become_enabled":{
            "title":"Become enabled",
            "type":"boolean",
            "x-nullable":true
        },
        "canceled_on":{
            "description":"The date and time when the cancel request was sent.",
            "format":"date-time",
            "readOnly":true,
            "title":"Canceled on",
            "type":"string",
            "x-nullable":true
        },
        "controller_node":{
            "description":"The instance that managed the execution environment.",
            "minLength":"1",
            "readOnly":true,
            "title":"Controller node",
            "type":"string"
        },
        "created":{
            "readOnly":true,
            "title":"Created",
            "type":"string"
        },
        "credential":{
            "title":"Credential",
            "type":"integer",
            "x-nullable":true
        },
        "diff_mode":{
            "title":"Diff mode",
            "type":"boolean",
            "x-nullable":true
        },
        "elapsed":{
            "description":"Elapsed time in seconds that the job ran.",
            "format":"decimal",
            "readOnly":true,
            "title":"Elapsed",
            "type":"string"
        },
        "execution_environment":{
            "description":"The container image to be used for execution.",
            "title":"Execution environment",
            "type":"integer",
            "x-nullable":true
        },
        "execution_node":{
            "description":"The node the job executed on.",
            "minLength":"1",
            "readOnly":true,
            "title":"Execution node",
            "type":"string"
        },
        "extra_vars":{
            "title":"Extra vars",
            "type":"string",
            "x-nullable":true
        },
        "failed":{
            "readOnly":true,
            "title":"Failed",
            "type":"boolean"
        },
        "finished":{
            "description":"The date and time the job finished execution.",
            "format":"date-time",
            "readOnly":true,
            "title":"Finished",
            "type":"string",
            "x-nullable":true
        },
        "forks":{
            "minimum":"0",
            "title":"Forks",
            "type":"integer"
        },
        "id":{
            "readOnly":true,
            "title":"ID",
            "type":"integer"
        },
        "inventory":{
            "title":"Inventory",
            "type":"integer",
            "x-nullable":true
        },
        "job_explanation":{
            "description":"A status field to indicate the state of the job if it wasn't able to run and capture stdout",
            "minLength":"1",
            "readOnly":true,
            "title":"Job explanation",
            "type":"string"
        },
        "job_type":{
            "default":"run",
            "enum":[
                "run",
                "check"
            ],
            "title":"Job type",
            "type":"string",
            "x-nullable":true
        },
        "launch_type":{
            "enum":[
                "manual",
                "relaunch",
                "callback",
                "scheduled",
                "dependency",
                "workflow",
                "webhook",
                "sync",
                "scm"
            ],
            "readOnly":true,
            "title":"Launch type",
            "type":"string"
        },
        "launched_by":{
            "readOnly":true,
            "title":"Launched by",
            "type":"string"
        },
        "limit":{
            "title":"Limit",
            "type":"string",
            "x-nullable":true
        },
        "modified":{
            "readOnly":true,
            "title":"Modified",
            "type":"string"
        },
        "module_args":{
            "title":"Module args",
            "type":"string",
            "x-nullable":true
        },
        "module_name":{
            "default":"command",
            "enum":[
                "command",
                "shell",
                "yum",
                "apt",
                "apt_key",
                "apt_repository",
                "apt_rpm",
                "service",
                "group",
                "user",
                "mount",
                "ping",
                "selinux",
                "setup",
                "win_ping",
                "win_service",
                "win_updates",
                "win_group",
                "win_user"
            ],
            "title":"Module name",
            "type":"string"
        },
        "name":{
            "minLength":"1",
            "readOnly":true,
            "title":"Name",
            "type":"string",
            "x-nullable":true
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "started":{
            "description":"The date and time the job was queued for starting.",
            "format":"date-time",
            "readOnly":true,
            "title":"Started",
            "type":"string",
            "x-nullable":true
        },
        "status":{
            "enum":[
                "new",
                "pending",
                "waiting",
                "running",
                "successful",
                "failed",
                "error",
                "canceled"
            ],
            "readOnly":true,
            "title":"Status",
            "type":"string"
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        },
        "verbosity":{
            "enum":[
                "0",
                "1",
                "2",
                "3",
                "4",
                "5"
            ],
            "title":"Verbosity",
            "type":"integer"
        },
        "work_unit_id":{
            "description":"The Receptor work unit ID associated with this job.",
            "minLength":"1",
            "readOnly":true,
            "title":"Work unit id",
            "type":"string",
            "x-nullable":true
        }
    },
    "type":"object"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-ad_hoc_commands-id-notifications-get.html -->

Make a GET request to this resource to retrieve a list of
notifications associated with the selected
ad hoc command.

The resulting data structure contains:

```
{
    "count": 99,
    "next": null,
    "previous": null,
    "results": [
        ...
    ]
}
```

The `count` field indicates the total number of notifications
found for the given query. The `next` and `previous` fields provides links to
additional results if there are more than will fit on a single page. The
`results` list contains zero or more notification records.

## Results

Each notification data structure includes the following fields:

- `id`: Database ID for this notification. (integer)
- `type`: Data type for this notification. (choice)
- `url`: URL for this notification. (string)
- `related`: Data structure with URLs of related resources. (object)
- `summary_fields`: Data structure with name/description for related resources. The output for some objects may be limited for performance reasons. (object)
- `created`: Timestamp when this notification was created. (datetime)
- `modified`: Timestamp when this notification was last modified. (datetime)
- `notification_template`: (id)
- `error`: (string)
- `status`: (choice)
  - `pending`: Pending
  - `successful`: Successful
  - `failed`: Failed
- `notifications_sent`: (integer)
- `notification_type`: (choice)
  - `email`: Email
  - `grafana`: Grafana
  - `irc`: IRC
  - `mattermost`: Mattermost
  - `pagerduty`: Pagerduty
  - `rocketchat`: Rocket.Chat
  - `slack`: Slack
  - `twilio`: Twilio
  - `webhook`: Webhook
- `recipients`: (string)
- `subject`: (string)
- `body`: Notification body (json)

## Sorting

To specify that notifications are returned in a particular
order, use the `order_by` query string parameter on the GET request.

```
?order_by=name
```

Prefix the field name with a dash `-` to sort in reverse:

```
?order_by=-name
```

Multiple sorting fields may be specified by separating the field names with a
comma `,`:

```
?order_by=name,some_other_field
```

## Pagination

Use the `page_size` query string parameter to change the number of results
returned for each request. Use the `page` query string parameter to retrieve
a particular page of results.

```
?page_size=100&page=2
```

The `previous` and `next` links returned with the results will set these query
string parameters automatically.

## Searching

Use the `search` query string parameter to perform a case-insensitive search
within all designated text fields of a model.

```
?search=findme
```

(*Added in Ansible Tower 3.1.0*) Search across related fields:

```
?related__search=findme
```

### Request

Supported Media Types

- application/json

Path Parameters

- [id(required): string](#request-path-param-0)

Query Parameters

- [page: integer](#request-query-param-0)

  A page number within the paginated result set.
- [page\_size: integer](#request-query-param-1)

  Number of results to return per page.
- [search: string](#request-query-param-2)

  A search term.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

Body ()

Root Schema : schema

Type: `object`

[Show Source](#)

- [count(required):
  integer](#200-paths--api-v2-ad_hoc_commands-{id}-notifications--get-responses-200-schema-properties-count-properties-count-0)
- [next:
  string(uri)](#200-paths--api-v2-ad_hoc_commands-{id}-notifications--get-responses-200-schema-properties-next-properties-next-0)
- [previous:
  string(uri)](#200-paths--api-v2-ad_hoc_commands-{id}-notifications--get-responses-200-schema-properties-previous-properties-previous-0)
- [results(required):
  array](#200-paths--api-v2-ad_hoc_commands-{id}-notifications--get-responses-200-schema-properties-results-properties-results-0)  [results](#200-paths--api-v2-ad_hoc_commands-{id}-notifications--get-responses-200-schema-properties-results)

```
{
    "properties":{
        "count":{
            "type":"integer"
        },
        "next":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "previous":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "results":{
            "items":{
                "$ref":"#/definitions/Notification"
            },
            "type":"array"
        }
    },
    "required":[
        "count",
        "results"
    ],
    "type":"object"
}
```

Nested Schema : results

Type: `array`

[Show Source](#)

- [Array of:
  object](#200-definitions-Notification-items-0)  [Notification](#200-definitions-Notification)

```
{
    "items":{
        "$ref":"#/definitions/Notification"
    },
    "type":"array"
}
```

Nested Schema : Notification

Type: `object`

[Show Source](#)

- [body:
  string](#200-definitions-Notification-properties-body-properties-body-0)

  Title: `Body`

  Read Only: `true`

  Notification body
- [created:
  string](#200-definitions-Notification-properties-created-properties-created-0)

  Title: `Created`

  Read Only: `true`
- [error:
  string](#200-definitions-Notification-properties-error-properties-error-0)

  Title: `Error`

  Read Only: `true`

  Minimum Length: `1`
- [id:
  integer](#200-definitions-Notification-properties-id-properties-id-0)

  Title: `ID`

  Read Only: `true`
- [modified:
  string](#200-definitions-Notification-properties-modified-properties-modified-0)

  Title: `Modified`

  Read Only: `true`
- [notification\_template:
  integer](#200-definitions-Notification-properties-notification_template-properties-notification_template-0)

  Title: `Notification template`

  Read Only: `true`
- [notification\_type(required):
  string](#200-definitions-Notification-properties-notification_type-properties-notification_type-0)

  Title: `Notification type`

  Allowed Values: `[
  "email",
  "grafana",
  "irc",
  "mattermost",
  "pagerduty",
  "rocketchat",
  "slack",
  "twilio",
  "webhook"
  ]`
- [notifications\_sent:
  integer](#200-definitions-Notification-properties-notifications_sent-properties-notifications_sent-0)

  Title: `Notifications sent`

  Read Only: `true`
- [recipients:
  string](#200-definitions-Notification-properties-recipients-properties-recipients-0)

  Title: `Recipients`

  Read Only: `true`

  Minimum Length: `1`
- [related:
  string](#200-definitions-Notification-properties-related-properties-related-0)

  Title: `Related`

  Read Only: `true`
- [status:
  string](#200-definitions-Notification-properties-status-properties-status-0)

  Title: `Status`

  Read Only: `true`

  Allowed Values: `[
  "pending",
  "successful",
  "failed"
  ]`
- [subject:
  string](#200-definitions-Notification-properties-subject-properties-subject-0)

  Title: `Subject`

  Read Only: `true`

  Minimum Length: `1`
- [summary\_fields:
  string](#200-definitions-Notification-properties-summary_fields-properties-summary_fields-0)

  Title: `Summary fields`

  Read Only: `true`
- [type:
  string](#200-definitions-Notification-properties-type-properties-type-0)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#200-definitions-Notification-properties-url-properties-url-0)

  Title: `Url`

  Read Only: `true`

```
{
    "properties":{
        "body":{
            "description":"Notification body",
            "readOnly":true,
            "title":"Body",
            "type":"string"
        },
        "created":{
            "readOnly":true,
            "title":"Created",
            "type":"string"
        },
        "error":{
            "minLength":"1",
            "readOnly":true,
            "title":"Error",
            "type":"string"
        },
        "id":{
            "readOnly":true,
            "title":"ID",
            "type":"integer"
        },
        "modified":{
            "readOnly":true,
            "title":"Modified",
            "type":"string"
        },
        "notification_template":{
            "readOnly":true,
            "title":"Notification template",
            "type":"integer"
        },
        "notification_type":{
            "enum":[
                "email",
                "grafana",
                "irc",
                "mattermost",
                "pagerduty",
                "rocketchat",
                "slack",
                "twilio",
                "webhook"
            ],
            "title":"Notification type",
            "type":"string",
            "x-nullable":true
        },
        "notifications_sent":{
            "readOnly":true,
            "title":"Notifications sent",
            "type":"integer"
        },
        "recipients":{
            "minLength":"1",
            "readOnly":true,
            "title":"Recipients",
            "type":"string"
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "status":{
            "enum":[
                "pending",
                "successful",
                "failed"
            ],
            "readOnly":true,
            "title":"Status",
            "type":"string"
        },
        "subject":{
            "minLength":"1",
            "readOnly":true,
            "title":"Subject",
            "type":"string"
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        }
    },
    "required":[
        "notification_type"
    ],
    "type":"object"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-ad_hoc_commands-id-relaunch-get.html -->

Make a POST request to this resource to launch a job. If any passwords or variables are required then they should be passed in via POST data. In order to determine what values are required in order to launch a job based on this job template you may make a GET request to this endpoint.

### Request

Supported Media Types

- application/json

Path Parameters

- [id(required): string](#request-path-param-0)

Query Parameters

- [page: integer](#request-query-param-0)

  A page number within the paginated result set.
- [page\_size: integer](#request-query-param-1)

  Number of results to return per page.
- [search: string](#request-query-param-2)

  A search term.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

Body ()

Root Schema : schema

Type: `object`

[Show Source](#)

- [count(required):
  integer](#200-paths--api-v2-ad_hoc_commands-{id}-relaunch--get-responses-200-schema-properties-count-properties-count-0)
- [next:
  string(uri)](#200-paths--api-v2-ad_hoc_commands-{id}-relaunch--get-responses-200-schema-properties-next-properties-next-0)
- [previous:
  string(uri)](#200-paths--api-v2-ad_hoc_commands-{id}-relaunch--get-responses-200-schema-properties-previous-properties-previous-0)
- [results(required):
  array](#200-paths--api-v2-ad_hoc_commands-{id}-relaunch--get-responses-200-schema-properties-results-properties-results-0)  [results](#200-paths--api-v2-ad_hoc_commands-{id}-relaunch--get-responses-200-schema-properties-results)

```
{
    "properties":{
        "count":{
            "type":"integer"
        },
        "next":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "previous":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "results":{
            "items":{
                "$ref":"#/definitions/AdHocCommandRelaunch"
            },
            "type":"array"
        }
    },
    "required":[
        "count",
        "results"
    ],
    "type":"object"
}
```

Nested Schema : results

Type: `array`

[Show Source](#)

- [Array of:
  object](#200-definitions-AdHocCommandRelaunch-items-0)  [AdHocCommandRelaunch](#200-definitions-AdHocCommandRelaunch)

```
{
    "items":{
        "$ref":"#/definitions/AdHocCommandRelaunch"
    },
    "type":"array"
}
```

Nested Schema : AdHocCommandRelaunch

Type: `object`

[Show Source](#)


```
{
    "properties":{
    },
    "type":"object"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-ad_hoc_commands-id-relaunch-post.html -->

Make a POST request to this resource to launch a job. If any passwords or variables are required then they should be passed in via POST data. In order to determine what values are required in order to launch a job based on this job template you may make a GET request to this endpoint.

### Request

Supported Media Types

- application/json

Path Parameters

- [id(required): string](#request-path-param-0)

Body ()

Root Schema : AdHocCommandRelaunch

Type: `object`

[Show Source](#)


```
{
    "properties":{
    },
    "type":"object"
}
```

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

Body ()

Root Schema : AdHocCommandRelaunch

Type: `object`

[Show Source](#)


```
{
    "properties":{
    },
    "type":"object"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-ad_hoc_commands-id-stdout-get.html -->

Make GET request to this resource to retrieve the stdout from running this
ad hoc command.

## Format

Use the `format` query string parameter to specify the output format.

- Browsable API: `?format=api`
- HTML: `?format=html`
- Plain Text: `?format=txt`
- Plain Text with ANSI color codes: `?format=ansi`
- JSON structure: `?format=json`
- Downloaded Plain Text: `?format=txt_download`
- Downloaded Plain Text with ANSI color codes: `?format=ansi_download`

(*New in Ansible Tower 2.0.0*) When using the Browsable API, HTML and JSON
formats, the `start_line` and `end_line` query string parameters can be used
to specify a range of line numbers to retrieve.

Use `dark=1` or `dark=0` as a query string parameter to force or disable a
dark background.

Files over 1.0??MB (configurable)
will not display in the browser. Use the `txt_download` or `ansi_download`
formats to download the file directly to view it.

### Request

Supported Media Types

- application/json

Path Parameters

- [id(required): string](#request-path-param-0)

[Back to Top](#top)

### Response

Supported Media Types

- application/json
- text/plain

#### 200 Response

Body ()

Root Schema : UnifiedJobStdout

Type: `object`

[Show Source](#)

- [result\_stdout:
  string](#200-definitions-UnifiedJobStdout-properties-result_stdout-properties-result_stdout-0)

  Title: `Result stdout`

  Read Only: `true`

```
{
    "properties":{
        "result_stdout":{
            "readOnly":true,
            "title":"Result stdout",
            "type":"string"
        }
    },
    "type":"object"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-ad_hoc_commands-id-get.html -->

Make GET request to this resource to retrieve a single ad hoc command
record containing the following fields:

- `id`: Database ID for this ad hoc command. (integer)
- `type`: Data type for this ad hoc command. (choice)
- `url`: URL for this ad hoc command. (string)
- `related`: Data structure with URLs of related resources. (object)
- `summary_fields`: Data structure with name/description for related resources. The output for some objects may be limited for performance reasons. (object)
- `created`: Timestamp when this ad hoc command was created. (datetime)
- `modified`: Timestamp when this ad hoc command was last modified. (datetime)
- `name`: Name of this ad hoc command. (string)
- `launch_type`: (choice)
  - `manual`: Manual
  - `relaunch`: Relaunch
  - `callback`: Callback
  - `scheduled`: Scheduled
  - `dependency`: Dependency
  - `workflow`: Workflow
  - `webhook`: Webhook
  - `sync`: Sync
  - `scm`: SCM Update
- `status`: (choice)
  - `new`: New
  - `pending`: Pending
  - `waiting`: Waiting
  - `running`: Running
  - `successful`: Successful
  - `failed`: Failed
  - `error`: Error
  - `canceled`: Canceled
- `execution_environment`: The container image to be used for execution. (id)
- `failed`: (boolean)
- `started`: The date and time the job was queued for starting. (datetime)
- `finished`: The date and time the job finished execution. (datetime)
- `canceled_on`: The date and time when the cancel request was sent. (datetime)
- `elapsed`: Elapsed time in seconds that the job ran. (decimal)
- `job_args`: (string)
- `job_cwd`: (string)
- `job_env`: (json)
- `job_explanation`: A status field to indicate the state of the job if it wasn't able to run and capture stdout (string)
- `execution_node`: The node the job executed on. (string)
- `controller_node`: The instance that managed the execution environment. (string)
- `result_traceback`: (string)
- `event_processing_finished`: Indicates whether all of the events generated by this unified job have been saved to the database. (boolean)
- `launched_by`: (field)
- `work_unit_id`: The Receptor work unit ID associated with this job. (string)
- `job_type`: (choice)
  - `run`: Run
  - `check`: Check
- `inventory`: (id)
- `limit`: (string)
- `credential`: (id)
- `module_name`: (choice)
  - `command`
  - `shell`
  - `yum`
  - `apt`
  - `apt_key`
  - `apt_repository`
  - `apt_rpm`
  - `service`
  - `group`
  - `user`
  - `mount`
  - `ping`
  - `selinux`
  - `setup`
  - `win_ping`
  - `win_service`
  - `win_updates`
  - `win_group`
  - `win_user`
- `module_args`: (string)
- `forks`: (integer)
- `verbosity`: (choice)
  - `0`: 0 (Normal)
  - `1`: 1 (Verbose)
  - `2`: 2 (More Verbose)
  - `3`: 3 (Debug)
  - `4`: 4 (Connection Debug)
  - `5`: 5 (WinRM Debug)
- `extra_vars`: (string)
- `become_enabled`: (boolean)
- `diff_mode`: (boolean)
- `host_status_counts`: Playbook stats from the Ansible playbook\_on\_stats event. (json)

### Request

Supported Media Types

- application/json

Path Parameters

- [id(required): string](#request-path-param-0)

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

Body ()

Root Schema : AdHocCommandDetail

Type: `object`

[Show Source](#)

- [become\_enabled:
  boolean](#200-definitions-AdHocCommandDetail-properties-become_enabled-properties-become_enabled-0)

  Title: `Become enabled`
- [canceled\_on:
  string(date-time)](#200-definitions-AdHocCommandDetail-properties-canceled_on-properties-canceled_on-0)

  Title: `Canceled on`

  Read Only: `true`

  The date and time when the cancel request was sent.
- [controller\_node:
  string](#200-definitions-AdHocCommandDetail-properties-controller_node-properties-controller_node-0)

  Title: `Controller node`

  Read Only: `true`

  Minimum Length: `1`

  The instance that managed the execution environment.
- [created:
  string](#200-definitions-AdHocCommandDetail-properties-created-properties-created-0)

  Title: `Created`

  Read Only: `true`
- [credential:
  integer](#200-definitions-AdHocCommandDetail-properties-credential-properties-credential-0)

  Title: `Credential`
- [diff\_mode:
  boolean](#200-definitions-AdHocCommandDetail-properties-diff_mode-properties-diff_mode-0)

  Title: `Diff mode`
- [elapsed:
  string(decimal)](#200-definitions-AdHocCommandDetail-properties-elapsed-properties-elapsed-0)

  Title: `Elapsed`

  Read Only: `true`

  Elapsed time in seconds that the job ran.
- [event\_processing\_finished:
  boolean](#200-definitions-AdHocCommandDetail-properties-event_processing_finished-properties-event_processing_finished-0)

  Title: `Event processing finished`

  Read Only: `true`

  Indicates whether all of the events generated by this unified job have been saved to the database.
- [execution\_environment:
  integer](#200-definitions-AdHocCommandDetail-properties-execution_environment-properties-execution_environment-0)

  Title: `Execution environment`

  The container image to be used for execution.
- [execution\_node:
  string](#200-definitions-AdHocCommandDetail-properties-execution_node-properties-execution_node-0)

  Title: `Execution node`

  Read Only: `true`

  Minimum Length: `1`

  The node the job executed on.
- [extra\_vars:
  string](#200-definitions-AdHocCommandDetail-properties-extra_vars-properties-extra_vars-0)

  Title: `Extra vars`
- [failed:
  boolean](#200-definitions-AdHocCommandDetail-properties-failed-properties-failed-0)

  Title: `Failed`

  Read Only: `true`
- [finished:
  string(date-time)](#200-definitions-AdHocCommandDetail-properties-finished-properties-finished-0)

  Title: `Finished`

  Read Only: `true`

  The date and time the job finished execution.
- [forks:
  integer](#200-definitions-AdHocCommandDetail-properties-forks-properties-forks-0)

  Title: `Forks`

  Minimum Value: `0`
- [host\_status\_counts:
  object](#200-definitions-AdHocCommandDetail-properties-host_status_counts-properties-host_status_counts-0)  [Host status counts](#200-definitions-AdHocCommandDetail-properties-host_status_counts)

  Title: `Host status counts`

  Read Only: `true`

  Playbook stats from the Ansible playbook\_on\_stats event.
- [id:
  integer](#200-definitions-AdHocCommandDetail-properties-id-properties-id-0)

  Title: `ID`

  Read Only: `true`
- [inventory:
  integer](#200-definitions-AdHocCommandDetail-properties-inventory-properties-inventory-0)

  Title: `Inventory`
- [job\_args:
  string](#200-definitions-AdHocCommandDetail-properties-job_args-properties-job_args-0)

  Title: `Job args`

  Read Only: `true`

  Minimum Length: `1`
- [job\_cwd:
  string](#200-definitions-AdHocCommandDetail-properties-job_cwd-properties-job_cwd-0)

  Title: `Job cwd`

  Read Only: `true`

  Minimum Length: `1`
- [job\_env:
  object](#200-definitions-AdHocCommandDetail-properties-job_env-properties-job_env-0)  [Job env](#200-definitions-AdHocCommandDetail-properties-job_env)

  Title: `Job env`

  Read Only: `true`
- [job\_explanation:
  string](#200-definitions-AdHocCommandDetail-properties-job_explanation-properties-job_explanation-0)

  Title: `Job explanation`

  Read Only: `true`

  Minimum Length: `1`

  A status field to indicate the state of the job if it wasn't able to run and capture stdout
- [job\_type:
  string](#200-definitions-AdHocCommandDetail-properties-job_type-properties-job_type-0)

  Title: `Job type`

  Default Value: `run`

  Allowed Values: `[
  "run",
  "check"
  ]`
- [launch\_type:
  string](#200-definitions-AdHocCommandDetail-properties-launch_type-properties-launch_type-0)

  Title: `Launch type`

  Read Only: `true`

  Allowed Values: `[
  "manual",
  "relaunch",
  "callback",
  "scheduled",
  "dependency",
  "workflow",
  "webhook",
  "sync",
  "scm"
  ]`
- [launched\_by:
  string](#200-definitions-AdHocCommandDetail-properties-launched_by-properties-launched_by-0)

  Title: `Launched by`

  Read Only: `true`
- [limit:
  string](#200-definitions-AdHocCommandDetail-properties-limit-properties-limit-0)

  Title: `Limit`
- [modified:
  string](#200-definitions-AdHocCommandDetail-properties-modified-properties-modified-0)

  Title: `Modified`

  Read Only: `true`
- [module\_args:
  string](#200-definitions-AdHocCommandDetail-properties-module_args-properties-module_args-0)

  Title: `Module args`
- [module\_name:
  string](#200-definitions-AdHocCommandDetail-properties-module_name-properties-module_name-0)

  Title: `Module name`

  Default Value: `command`

  Allowed Values: `[
  "command",
  "shell",
  "yum",
  "apt",
  "apt_key",
  "apt_repository",
  "apt_rpm",
  "service",
  "group",
  "user",
  "mount",
  "ping",
  "selinux",
  "setup",
  "win_ping",
  "win_service",
  "win_updates",
  "win_group",
  "win_user"
  ]`
- [name:
  string](#200-definitions-AdHocCommandDetail-properties-name-properties-name-0)

  Title: `Name`

  Read Only: `true`

  Minimum Length: `1`
- [related:
  string](#200-definitions-AdHocCommandDetail-properties-related-properties-related-0)

  Title: `Related`

  Read Only: `true`
- [result\_traceback:
  string](#200-definitions-AdHocCommandDetail-properties-result_traceback-properties-result_traceback-0)

  Title: `Result traceback`

  Read Only: `true`

  Minimum Length: `1`
- [started:
  string(date-time)](#200-definitions-AdHocCommandDetail-properties-started-properties-started-0)

  Title: `Started`

  Read Only: `true`

  The date and time the job was queued for starting.
- [status:
  string](#200-definitions-AdHocCommandDetail-properties-status-properties-status-0)

  Title: `Status`

  Read Only: `true`

  Allowed Values: `[
  "new",
  "pending",
  "waiting",
  "running",
  "successful",
  "failed",
  "error",
  "canceled"
  ]`
- [summary\_fields:
  string](#200-definitions-AdHocCommandDetail-properties-summary_fields-properties-summary_fields-0)

  Title: `Summary fields`

  Read Only: `true`
- [type:
  string](#200-definitions-AdHocCommandDetail-properties-type-properties-type-0)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#200-definitions-AdHocCommandDetail-properties-url-properties-url-0)

  Title: `Url`

  Read Only: `true`
- [verbosity:
  integer](#200-definitions-AdHocCommandDetail-properties-verbosity-properties-verbosity-0)

  Title: `Verbosity`

  Allowed Values: `[
  "0",
  "1",
  "2",
  "3",
  "4",
  "5"
  ]`
- [work\_unit\_id:
  string](#200-definitions-AdHocCommandDetail-properties-work_unit_id-properties-work_unit_id-0)

  Title: `Work unit id`

  Read Only: `true`

  Minimum Length: `1`

  The Receptor work unit ID associated with this job.

```
{
    "properties":{
        "become_enabled":{
            "title":"Become enabled",
            "type":"boolean",
            "x-nullable":true
        },
        "canceled_on":{
            "description":"The date and time when the cancel request was sent.",
            "format":"date-time",
            "readOnly":true,
            "title":"Canceled on",
            "type":"string",
            "x-nullable":true
        },
        "controller_node":{
            "description":"The instance that managed the execution environment.",
            "minLength":"1",
            "readOnly":true,
            "title":"Controller node",
            "type":"string"
        },
        "created":{
            "readOnly":true,
            "title":"Created",
            "type":"string"
        },
        "credential":{
            "title":"Credential",
            "type":"integer",
            "x-nullable":true
        },
        "diff_mode":{
            "title":"Diff mode",
            "type":"boolean",
            "x-nullable":true
        },
        "elapsed":{
            "description":"Elapsed time in seconds that the job ran.",
            "format":"decimal",
            "readOnly":true,
            "title":"Elapsed",
            "type":"string"
        },
        "event_processing_finished":{
            "description":"Indicates whether all of the events generated by this unified job have been saved to the database.",
            "readOnly":true,
            "title":"Event processing finished",
            "type":"boolean"
        },
        "execution_environment":{
            "description":"The container image to be used for execution.",
            "title":"Execution environment",
            "type":"integer",
            "x-nullable":true
        },
        "execution_node":{
            "description":"The node the job executed on.",
            "minLength":"1",
            "readOnly":true,
            "title":"Execution node",
            "type":"string"
        },
        "extra_vars":{
            "title":"Extra vars",
            "type":"string",
            "x-nullable":true
        },
        "failed":{
            "readOnly":true,
            "title":"Failed",
            "type":"boolean"
        },
        "finished":{
            "description":"The date and time the job finished execution.",
            "format":"date-time",
            "readOnly":true,
            "title":"Finished",
            "type":"string",
            "x-nullable":true
        },
        "forks":{
            "minimum":"0",
            "title":"Forks",
            "type":"integer"
        },
        "host_status_counts":{
            "description":"Playbook stats from the Ansible playbook_on_stats event.",
            "readOnly":true,
            "title":"Host status counts",
            "type":"object",
            "x-nullable":true
        },
        "id":{
            "readOnly":true,
            "title":"ID",
            "type":"integer"
        },
        "inventory":{
            "title":"Inventory",
            "type":"integer",
            "x-nullable":true
        },
        "job_args":{
            "minLength":"1",
            "readOnly":true,
            "title":"Job args",
            "type":"string"
        },
        "job_cwd":{
            "minLength":"1",
            "readOnly":true,
            "title":"Job cwd",
            "type":"string"
        },
        "job_env":{
            "readOnly":true,
            "title":"Job env",
            "type":"object"
        },
        "job_explanation":{
            "description":"A status field to indicate the state of the job if it wasn't able to run and capture stdout",
            "minLength":"1",
            "readOnly":true,
            "title":"Job explanation",
            "type":"string"
        },
        "job_type":{
            "default":"run",
            "enum":[
                "run",
                "check"
            ],
            "title":"Job type",
            "type":"string",
            "x-nullable":true
        },
        "launch_type":{
            "enum":[
                "manual",
                "relaunch",
                "callback",
                "scheduled",
                "dependency",
                "workflow",
                "webhook",
                "sync",
                "scm"
            ],
            "readOnly":true,
            "title":"Launch type",
            "type":"string"
        },
        "launched_by":{
            "readOnly":true,
            "title":"Launched by",
            "type":"string"
        },
        "limit":{
            "title":"Limit",
            "type":"string",
            "x-nullable":true
        },
        "modified":{
            "readOnly":true,
            "title":"Modified",
            "type":"string"
        },
        "module_args":{
            "title":"Module args",
            "type":"string",
            "x-nullable":true
        },
        "module_name":{
            "default":"command",
            "enum":[
                "command",
                "shell",
                "yum",
                "apt",
                "apt_key",
                "apt_repository",
                "apt_rpm",
                "service",
                "group",
                "user",
                "mount",
                "ping",
                "selinux",
                "setup",
                "win_ping",
                "win_service",
                "win_updates",
                "win_group",
                "win_user"
            ],
            "title":"Module name",
            "type":"string"
        },
        "name":{
            "minLength":"1",
            "readOnly":true,
            "title":"Name",
            "type":"string",
            "x-nullable":true
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "result_traceback":{
            "minLength":"1",
            "readOnly":true,
            "title":"Result traceback",
            "type":"string"
        },
        "started":{
            "description":"The date and time the job was queued for starting.",
            "format":"date-time",
            "readOnly":true,
            "title":"Started",
            "type":"string",
            "x-nullable":true
        },
        "status":{
            "enum":[
                "new",
                "pending",
                "waiting",
                "running",
                "successful",
                "failed",
                "error",
                "canceled"
            ],
            "readOnly":true,
            "title":"Status",
            "type":"string"
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        },
        "verbosity":{
            "enum":[
                "0",
                "1",
                "2",
                "3",
                "4",
                "5"
            ],
            "title":"Verbosity",
            "type":"integer"
        },
        "work_unit_id":{
            "description":"The Receptor work unit ID associated with this job.",
            "minLength":"1",
            "readOnly":true,
            "title":"Work unit id",
            "type":"string",
            "x-nullable":true
        }
    },
    "type":"object"
}
```

Nested Schema : Host status counts

Type: `object`

Title: `Host status counts`

Read Only: `true`

Playbook stats from the Ansible playbook\_on\_stats event.

Nested Schema : Job env

Type: `object`

Title: `Job env`

Read Only: `true`

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-ad_hoc_commands-id-cancel-get.html -->

Make GET request to this resource to retrieve a single ad hoc command
record containing the following fields:

- `can_cancel`: (boolean)

### Request

Supported Media Types

- application/json

Path Parameters

- [id(required): string](#request-path-param-0)

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

Body ()

Root Schema : AdHocCommandCancel

Type: `object`

[Show Source](#)

- [can\_cancel:
  boolean](#200-definitions-AdHocCommandCancel-properties-can_cancel-properties-can_cancel-0)

  Title: `Can cancel`

  Read Only: `true`

```
{
    "properties":{
        "can_cancel":{
            "readOnly":true,
            "title":"Can cancel",
            "type":"boolean"
        }
    },
    "type":"object"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-ad_hoc_commands-id-cancel-post.html -->

Make GET request to this resource to retrieve a single ad hoc command
record containing the following fields:

- `can_cancel`: (boolean)

### Request

Supported Media Types

- application/json

Path Parameters

- [id(required): string](#request-path-param-0)

Body ()

Root Schema : AdHocCommandCancel

Type: `object`

[Show Source](#)

- [can\_cancel:
  boolean](#request-bodyparam-definitions-AdHocCommandCancel-properties-can_cancel-properties-can_cancel-0)

  Title: `Can cancel`

  Read Only: `true`

```
{
    "properties":{
        "can_cancel":{
            "readOnly":true,
            "title":"Can cancel",
            "type":"boolean"
        }
    },
    "type":"object"
}
```

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

Body ()

Root Schema : AdHocCommandCancel

Type: `object`

[Show Source](#)

- [can\_cancel:
  boolean](#201-definitions-AdHocCommandCancel-properties-can_cancel-properties-can_cancel-0)

  Title: `Can cancel`

  Read Only: `true`

```
{
    "properties":{
        "can_cancel":{
            "readOnly":true,
            "title":"Can cancel",
            "type":"boolean"
        }
    },
    "type":"object"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/api-analytics.html -->

Sort by

Task

 Path

 Method

Analytics

REST API endpoints for Analytics

[Analytics Adoption Rate Create](op-api-v2-analytics-adoption_rate-post.html)
:   Method: post

    Path: `/api/v2/analytics/adoption_rate/`

[Analytics Adoption Rate List](op-api-v2-analytics-adoption_rate-get.html)
:   Method: get

    Path: `/api/v2/analytics/adoption_rate/`

[Analytics Adoption Rate Options Create](op-api-v2-analytics-adoption_rate_options-post.html)
:   Method: post

    Path: `/api/v2/analytics/adoption_rate_options/`

[Analytics Adoption Rate Options List](op-api-v2-analytics-adoption_rate_options-get.html)
:   Method: get

    Path: `/api/v2/analytics/adoption_rate_options/`

[Analytics Authorized Create](op-api-v2-analytics-authorized-post.html)
:   Method: post

    Path: `/api/v2/analytics/authorized/`

[Analytics Authorized List](op-api-v2-analytics-authorized-get.html)
:   Method: get

    Path: `/api/v2/analytics/authorized/`

[Analytics Event Explorer Create](op-api-v2-analytics-event_explorer-post.html)
:   Method: post

    Path: `/api/v2/analytics/event_explorer/`

[Analytics Event Explorer List](op-api-v2-analytics-event_explorer-get.html)
:   Method: get

    Path: `/api/v2/analytics/event_explorer/`

[Analytics Event Explorer Options Create](op-api-v2-analytics-event_explorer_options-post.html)
:   Method: post

    Path: `/api/v2/analytics/event_explorer_options/`

[Analytics Event Explorer Options List](op-api-v2-analytics-event_explorer_options-get.html)
:   Method: get

    Path: `/api/v2/analytics/event_explorer_options/`

[Analytics Host Explorer Create](op-api-v2-analytics-host_explorer-post.html)
:   Method: post

    Path: `/api/v2/analytics/host_explorer/`

[Analytics Host Explorer List](op-api-v2-analytics-host_explorer-get.html)
:   Method: get

    Path: `/api/v2/analytics/host_explorer/`

[Analytics Host Explorer Options Create](op-api-v2-analytics-host_explorer_options-post.html)
:   Method: post

    Path: `/api/v2/analytics/host_explorer_options/`

[Analytics Host Explorer Options List](op-api-v2-analytics-host_explorer_options-get.html)
:   Method: get

    Path: `/api/v2/analytics/host_explorer_options/`

[Analytics Job Explorer Create](op-api-v2-analytics-job_explorer-post.html)
:   Method: post

    Path: `/api/v2/analytics/job_explorer/`

[Analytics Job Explorer List](op-api-v2-analytics-job_explorer-get.html)
:   Method: get

    Path: `/api/v2/analytics/job_explorer/`

[Analytics Job Explorer Options Create](op-api-v2-analytics-job_explorer_options-post.html)
:   Method: post

    Path: `/api/v2/analytics/job_explorer_options/`

[Analytics Job Explorer Options List](op-api-v2-analytics-job_explorer_options-get.html)
:   Method: get

    Path: `/api/v2/analytics/job_explorer_options/`

[Analytics List](op-api-v2-analytics-get.html)
:   Method: get

    Path: `/api/v2/analytics/`

[Analytics Probe Template for Hosts Create](op-api-v2-analytics-probe_template_for_hosts-post.html)
:   Method: post

    Path: `/api/v2/analytics/probe_template_for_hosts/`

[Analytics Probe Template for Hosts List](op-api-v2-analytics-probe_template_for_hosts-get.html)
:   Method: get

    Path: `/api/v2/analytics/probe_template_for_hosts/`

[Analytics Probe Template for Hosts Options Create](op-api-v2-analytics-probe_template_for_hosts_options-post.html)
:   Method: post

    Path: `/api/v2/analytics/probe_template_for_hosts_options/`

[Analytics Probe Template for Hosts Options List](op-api-v2-analytics-probe_template_for_hosts_options-get.html)
:   Method: get

    Path: `/api/v2/analytics/probe_template_for_hosts_options/`

[Analytics Probe Templates Create](op-api-v2-analytics-probe_templates-post.html)
:   Method: post

    Path: `/api/v2/analytics/probe_templates/`

[Analytics Probe Templates List](op-api-v2-analytics-probe_templates-get.html)
:   Method: get

    Path: `/api/v2/analytics/probe_templates/`

[Analytics Probe Templates Options Create](op-api-v2-analytics-probe_templates_options-post.html)
:   Method: post

    Path: `/api/v2/analytics/probe_templates_options/`

[Analytics Probe Templates Options List](op-api-v2-analytics-probe_templates_options-get.html)
:   Method: get

    Path: `/api/v2/analytics/probe_templates_options/`

[Analytics Report Create](op-api-v2-analytics-report-slug-post.html)
:   Method: post

    Path: `/api/v2/analytics/report/{slug}/`

[Analytics Report Options Create](op-api-v2-analytics-report_options-post.html)
:   Method: post

    Path: `/api/v2/analytics/report_options/`

[Analytics Report Options List](op-api-v2-analytics-report_options-get.html)
:   Method: get

    Path: `/api/v2/analytics/report_options/`

[Analytics Report Read](op-api-v2-analytics-report-slug-get.html)
:   Method: get

    Path: `/api/v2/analytics/report/{slug}/`

[Analytics Reports Create](op-api-v2-analytics-reports-post.html)
:   Method: post

    Path: `/api/v2/analytics/reports/`

[Analytics Reports List](op-api-v2-analytics-reports-get.html)
:   Method: get

    Path: `/api/v2/analytics/reports/`

[Analytics Roi Templates Create](op-api-v2-analytics-roi_templates-post.html)
:   Method: post

    Path: `/api/v2/analytics/roi_templates/`

[Analytics Roi Templates List](op-api-v2-analytics-roi_templates-get.html)
:   Method: get

    Path: `/api/v2/analytics/roi_templates/`

[Analytics Roi Templates Options Create](op-api-v2-analytics-roi_templates_options-post.html)
:   Method: post

    Path: `/api/v2/analytics/roi_templates_options/`

[Analytics Roi Templates Options List](op-api-v2-analytics-roi_templates_options-get.html)
:   Method: get

    Path: `/api/v2/analytics/roi_templates_options/`


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-adoption_rate-post.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-adoption_rate-get.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-adoption_rate_options-post.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-adoption_rate_options-get.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-authorized-post.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-authorized-get.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-event_explorer-post.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-event_explorer-get.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-event_explorer_options-post.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-event_explorer_options-get.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-host_explorer-post.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-host_explorer-get.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-host_explorer_options-post.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-host_explorer_options-get.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-job_explorer-post.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-job_explorer-get.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-job_explorer_options-post.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-job_explorer_options-get.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-get.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-probe_template_for_hosts-post.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-probe_template_for_hosts-get.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-probe_template_for_hosts_options-post.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-probe_template_for_hosts_options-get.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-probe_templates-post.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-probe_templates-get.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-probe_templates_options-post.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-probe_templates_options-get.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-report-slug-post.html -->

### Request

Supported Media Types

- application/json

Path Parameters

- [slug(required): string](#request-path-param-0)

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-report_options-post.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-report_options-get.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-report-slug-get.html -->

### Request

Supported Media Types

- application/json

Path Parameters

- [slug(required): string](#request-path-param-0)

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-reports-post.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-reports-get.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-roi_templates-post.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-roi_templates-get.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-roi_templates_options-post.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-analytics-roi_templates_options-get.html -->

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/api-api.html -->

Sort by

Task

 Path

 Method

API

The operations from the API category.

[Debug List](op-api-debug-get.html)
:   Method: get

    Path: `/api/debug/`

[List](op-api-get.html)
:   Method: get

    Path: `/api/`

[Read](op-api-v2-get.html)
:   Method: get

    Path: `/api/v2/`

[Token Handling Using OAuth2](op-api-o-get.html)
:   Method: get

    Path: `/api/o/`


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-debug-get.html -->

List of available debug urls

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-get.html -->

List supported API versions

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

Body

Example Response (application/json)

```
{
    "available_versions":{
        "v2":"/api/v2/"
    },
    "current_version":"/api/v2/",
    "custom_login_info":"",
    "custom_logo":"",
    "description":"Oracle Linux Automation Manager REST API",
    "login_redirect_override":"",
    "oauth2":"/api/o/",
    "swagger":"/api/swagger/"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-get.html -->

List top level resources

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

Body

Example Response (application/json)

```
{
    "activity_stream":"/api/v2/activity_stream/",
    "ad_hoc_commands":"/api/v2/ad_hoc_commands/",
    "analytics":"/api/v2/analytics/",
    "applications":"/api/v2/applications/",
    "bulk":"/api/v2/bulk/",
    "config":"/api/v2/config/",
    "constructed_inventory":"/api/v2/constructed_inventories/",
    "credential_input_sources":"/api/v2/credential_input_sources/",
    "credential_types":"/api/v2/credential_types/",
    "credentials":"/api/v2/credentials/",
    "dashboard":"/api/v2/dashboard/",
    "execution_environments":"/api/v2/execution_environments/",
    "groups":"/api/v2/groups/",
    "host_metric_summary_monthly":"/api/v2/host_metric_summary_monthly/",
    "host_metrics":"/api/v2/host_metrics/",
    "hosts":"/api/v2/hosts/",
    "instance_groups":"/api/v2/instance_groups/",
    "instances":"/api/v2/instances/",
    "inventory":"/api/v2/inventories/",
    "inventory_sources":"/api/v2/inventory_sources/",
    "inventory_updates":"/api/v2/inventory_updates/",
    "job_templates":"/api/v2/job_templates/",
    "jobs":"/api/v2/jobs/",
    "labels":"/api/v2/labels/",
    "me":"/api/v2/me/",
    "mesh_visualizer":"/api/v2/mesh_visualizer/",
    "metrics":"/api/v2/metrics/",
    "notification_templates":"/api/v2/notification_templates/",
    "notifications":"/api/v2/notifications/",
    "organizations":"/api/v2/organizations/",
    "ping":"/api/v2/ping/",
    "project_updates":"/api/v2/project_updates/",
    "projects":"/api/v2/projects/",
    "roles":"/api/v2/roles/",
    "schedules":"/api/v2/schedules/",
    "settings":"/api/v2/settings/",
    "system_job_templates":"/api/v2/system_job_templates/",
    "system_jobs":"/api/v2/system_jobs/",
    "teams":"/api/v2/teams/",
    "tokens":"/api/v2/tokens/",
    "unified_job_templates":"/api/v2/unified_job_templates/",
    "unified_jobs":"/api/v2/unified_jobs/",
    "users":"/api/v2/users/",
    "workflow_approvals":"/api/v2/workflow_approvals/",
    "workflow_job_nodes":"/api/v2/workflow_job_nodes/",
    "workflow_job_template_nodes":"/api/v2/workflow_job_template_nodes/",
    "workflow_job_templates":"/api/v2/workflow_job_templates/",
    "workflow_jobs":"/api/v2/workflow_jobs/"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-o-get.html -->

This page lists OAuth 2 utility endpoints used for authorization, token refresh and revoke.
Note endpoints other than `/api/o/authorize/` are not meant to be used in browsers and do not
support HTTP GET. The endpoints here strictly follow
[RFC specs for OAuth2](https://tools.ietf.org/html/rfc6749), so please use that for detailed
reference. Note AWX net location default to `http://localhost:8013` in examples:

## Create Token for an Application using Authorization code grant type

Given an application "AuthCodeApp" of grant type `authorization-code`,
from the client app, the user makes a GET to the Authorize endpoint with

- `response_type`
- `client_id`
- `redirect_uris`
- `scope`

AWX will respond with the authorization `code` and `state`
to the redirect\_uri specified in the application. The client application will then make a POST to the
`api/o/token/` endpoint on AWX with

- `code`
- `client_id`
- `client_secret`
- `grant_type`
- `redirect_uri`

AWX will respond with the `access_token`, `token_type`, `refresh_token`, and `expires_in`. For more
information on testing this flow, refer to [django-oauth-toolkit](http://django-oauth-toolkit.readthedocs.io/en/latest/tutorial/tutorial_01.html#test-your-authorization-server).

## Create Token for an Application using Password grant type

Log in is not required for `password` grant type, so a simple `curl` can be used to acquire a personal access token
via `/api/o/token/` with

- `grant_type`: Required to be "password"
- `username`
- `password`
- `client_id`: Associated application must have grant\_type "password"
- `client_secret`

For example:

```
curl -X POST \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=password&username=<username>&password=<password>&scope=read" \
  -u "gwSPoasWSdNkMDtBN3Hu2WYQpPWCO9SwUEsKK22l:fI6ZpfocHYBGfm1tP92r0yIgCyfRdDQt0Tos9L8a4fNsJjQQMwp9569e
IaUBsaVDgt2eiwOGe0bg5m5vCSstClZmtdy359RVx2rQK5YlIWyPlrolpt2LEpVeKXWaiybo" \
  http://localhost:8013/api/o/token/ -i
```

In the above post request, parameters `username` and `password` are username and password of the related
AWX user of the underlying application, and the authentication information is of format
`<client_id>:<client_secret>`, where `client_id` and `client_secret` are the corresponding fields of
underlying application.

Upon success, access token, refresh token and other information are given in the response body in JSON

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/api-applications.html -->

Sort by

Task

 Path

 Method

Applications

REST API endpoints for Applications

[Create an Access Token for an Application](op-api-v2-applications-id-tokens-post.html)
:   Method: post

    Path: `/api/v2/applications/{id}/tokens/`

[Create an Application](op-api-v2-applications-post.html)
:   Method: post

    Path: `/api/v2/applications/`

[Delete an Application](op-api-v2-applications-id-delete.html)
:   Method: delete

    Path: `/api/v2/applications/{id}/`

[List Access Tokens for an Application](op-api-v2-applications-id-tokens-get.html)
:   Method: get

    Path: `/api/v2/applications/{id}/tokens/`

[List Activity Streams for an Application](op-api-v2-applications-id-activity_stream-get.html)
:   Method: get

    Path: `/api/v2/applications/{id}/activity_stream/`

[List Applications](op-api-v2-applications-get.html)
:   Method: get

    Path: `/api/v2/applications/`

[Retrieve an Application](op-api-v2-applications-id-get.html)
:   Method: get

    Path: `/api/v2/applications/{id}/`

[Update an Application](op-api-v2-applications-id-patch.html)
:   Method: patch

    Path: `/api/v2/applications/{id}/`

[Update an Application](op-api-v2-applications-id-put.html)
:   Method: put

    Path: `/api/v2/applications/{id}/`


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-applications-id-tokens-post.html -->

Make a POST request to this resource with the following access token
fields to create a new access token associated with this
application.

- `description`: Optional description of this access token. (string, default=`""`)
- `scope`: Allowed scopes, further restricts user's permissions. Must be a simple space-separated string with allowed scopes ['read', 'write']. (string, default=`"write"`)

### Request

Supported Media Types

- application/json

Path Parameters

- [id(required): string](#request-path-param-0)

Body ()

Root Schema : OAuth2Token

Type: `object`

[Show Source](#)

- [application:
  integer](#request-bodyparam-definitions-OAuth2Token-properties-application-properties-application-0)

  Title: `Application`
- [created:
  string](#request-bodyparam-definitions-OAuth2Token-properties-created-properties-created-0)

  Title: `Created`

  Read Only: `true`
- [description:
  string](#request-bodyparam-definitions-OAuth2Token-properties-description-properties-description-0)

  Title: `Description`
- [expires:
  string(date-time)](#request-bodyparam-definitions-OAuth2Token-properties-expires-properties-expires-0)

  Title: `Expires`

  Read Only: `true`
- [id:
  integer](#request-bodyparam-definitions-OAuth2Token-properties-id-properties-id-0)

  Title: `Id`

  Read Only: `true`
- [modified:
  string](#request-bodyparam-definitions-OAuth2Token-properties-modified-properties-modified-0)

  Title: `Modified`

  Read Only: `true`
- [refresh\_token:
  string](#request-bodyparam-definitions-OAuth2Token-properties-refresh_token-properties-refresh_token-0)

  Title: `Refresh token`

  Read Only: `true`
- [related:
  string](#request-bodyparam-definitions-OAuth2Token-properties-related-properties-related-0)

  Title: `Related`

  Read Only: `true`
- [scope:
  string](#request-bodyparam-definitions-OAuth2Token-properties-scope-properties-scope-0)

  Title: `Scope`

  Default Value: `write`

  Allowed scopes, further restricts user's permissions. Must be a simple space-separated string with allowed scopes ['read', 'write'].
- [summary\_fields:
  string](#request-bodyparam-definitions-OAuth2Token-properties-summary_fields-properties-summary_fields-0)

  Title: `Summary fields`

  Read Only: `true`
- [token:
  string](#request-bodyparam-definitions-OAuth2Token-properties-token-properties-token-0)

  Title: `Token`

  Read Only: `true`
- [type:
  string](#request-bodyparam-definitions-OAuth2Token-properties-type-properties-type-0)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#request-bodyparam-definitions-OAuth2Token-properties-url-properties-url-0)

  Title: `Url`

  Read Only: `true`
- [user:
  integer](#request-bodyparam-definitions-OAuth2Token-properties-user-properties-user-0)

  Title: `User`

  Read Only: `true`

  The user representing the token owner

```
{
    "properties":{
        "application":{
            "title":"Application",
            "type":"integer",
            "x-nullable":true
        },
        "created":{
            "readOnly":true,
            "title":"Created",
            "type":"string"
        },
        "description":{
            "title":"Description",
            "type":"string",
            "x-nullable":true
        },
        "expires":{
            "format":"date-time",
            "readOnly":true,
            "title":"Expires",
            "type":"string"
        },
        "id":{
            "readOnly":true,
            "title":"Id",
            "type":"integer"
        },
        "modified":{
            "readOnly":true,
            "title":"Modified",
            "type":"string"
        },
        "refresh_token":{
            "readOnly":true,
            "title":"Refresh token",
            "type":"string"
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "scope":{
            "default":"write",
            "description":"Allowed scopes, further restricts user's permissions. Must be a simple space-separated string with allowed scopes ['read', 'write'].",
            "title":"Scope",
            "type":"string",
            "x-nullable":true
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "token":{
            "readOnly":true,
            "title":"Token",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        },
        "user":{
            "description":"The user representing the token owner",
            "readOnly":true,
            "title":"User",
            "type":"integer"
        }
    },
    "type":"object"
}
```

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

Body ()

Root Schema : OAuth2Token

Type: `object`

[Show Source](#)

- [application:
  integer](#201-definitions-OAuth2Token-properties-application-properties-application-0)

  Title: `Application`
- [created:
  string](#201-definitions-OAuth2Token-properties-created-properties-created-0)

  Title: `Created`

  Read Only: `true`
- [description:
  string](#201-definitions-OAuth2Token-properties-description-properties-description-0)

  Title: `Description`
- [expires:
  string(date-time)](#201-definitions-OAuth2Token-properties-expires-properties-expires-0)

  Title: `Expires`

  Read Only: `true`
- [id:
  integer](#201-definitions-OAuth2Token-properties-id-properties-id-0)

  Title: `Id`

  Read Only: `true`
- [modified:
  string](#201-definitions-OAuth2Token-properties-modified-properties-modified-0)

  Title: `Modified`

  Read Only: `true`
- [refresh\_token:
  string](#201-definitions-OAuth2Token-properties-refresh_token-properties-refresh_token-0)

  Title: `Refresh token`

  Read Only: `true`
- [related:
  string](#201-definitions-OAuth2Token-properties-related-properties-related-0)

  Title: `Related`

  Read Only: `true`
- [scope:
  string](#201-definitions-OAuth2Token-properties-scope-properties-scope-0)

  Title: `Scope`

  Default Value: `write`

  Allowed scopes, further restricts user's permissions. Must be a simple space-separated string with allowed scopes ['read', 'write'].
- [summary\_fields:
  string](#201-definitions-OAuth2Token-properties-summary_fields-properties-summary_fields-0)

  Title: `Summary fields`

  Read Only: `true`
- [token:
  string](#201-definitions-OAuth2Token-properties-token-properties-token-0)

  Title: `Token`

  Read Only: `true`
- [type:
  string](#201-definitions-OAuth2Token-properties-type-properties-type-0)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#201-definitions-OAuth2Token-properties-url-properties-url-0)

  Title: `Url`

  Read Only: `true`
- [user:
  integer](#201-definitions-OAuth2Token-properties-user-properties-user-0)

  Title: `User`

  Read Only: `true`

  The user representing the token owner

```
{
    "properties":{
        "application":{
            "title":"Application",
            "type":"integer",
            "x-nullable":true
        },
        "created":{
            "readOnly":true,
            "title":"Created",
            "type":"string"
        },
        "description":{
            "title":"Description",
            "type":"string",
            "x-nullable":true
        },
        "expires":{
            "format":"date-time",
            "readOnly":true,
            "title":"Expires",
            "type":"string"
        },
        "id":{
            "readOnly":true,
            "title":"Id",
            "type":"integer"
        },
        "modified":{
            "readOnly":true,
            "title":"Modified",
            "type":"string"
        },
        "refresh_token":{
            "readOnly":true,
            "title":"Refresh token",
            "type":"string"
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "scope":{
            "default":"write",
            "description":"Allowed scopes, further restricts user's permissions. Must be a simple space-separated string with allowed scopes ['read', 'write'].",
            "title":"Scope",
            "type":"string",
            "x-nullable":true
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "token":{
            "readOnly":true,
            "title":"Token",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        },
        "user":{
            "description":"The user representing the token owner",
            "readOnly":true,
            "title":"User",
            "type":"integer"
        }
    },
    "type":"object"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-applications-post.html -->

Make a POST request to this resource with the following application
fields to create a new application:

- `name`: Name of this application. (string, required)
- `description`: Optional description of this application. (string, default=`""`)
- `client_type`: Set to Public or Confidential depending on how secure the client device is. (choice, required)

  - `confidential`: Confidential
  - `public`: Public
- `redirect_uris`: Allowed URIs list, space separated (string, default=`""`)
- `authorization_grant_type`: The Grant type the user must use for acquire tokens for this application. (choice, required)
  - `authorization-code`: Authorization code
  - `password`: Resource owner password-based
- `skip_authorization`: Set True to skip authorization step for completely trusted applications. (boolean, default=`False`)
- `organization`: Organization containing this application. (id, required)

### Request

Supported Media Types

- application/json

Body ()

Root Schema : OAuth2Application

Type: `object`

[Show Source](#)

- [authorization\_grant\_type(required):
  string](#request-bodyparam-definitions-OAuth2Application-properties-authorization_grant_type-properties-authorization_grant_type-0)

  Title: `Authorization Grant Type`

  Allowed Values: `[
  "authorization-code",
  "password"
  ]`

  The Grant type the user must use for acquire tokens for this application.
- [client\_id:
  string](#request-bodyparam-definitions-OAuth2Application-properties-client_id-properties-client_id-0)

  Title: `Client id`

  Read Only: `true`

  Minimum Length: `1`
- [client\_secret:
  string](#request-bodyparam-definitions-OAuth2Application-properties-client_secret-properties-client_secret-0)

  Title: `Client Secret`

  Read Only: `true`

  Minimum Length: `1`

  Used for more stringent verification of access to an application when creating a token.
- [client\_type(required):
  string](#request-bodyparam-definitions-OAuth2Application-properties-client_type-properties-client_type-0)

  Title: `Client Type`

  Allowed Values: `[
  "confidential",
  "public"
  ]`

  Set to Public or Confidential depending on how secure the client device is.
- [created:
  string](#request-bodyparam-definitions-OAuth2Application-properties-created-properties-created-0)

  Title: `Created`

  Read Only: `true`
- [description:
  string](#request-bodyparam-definitions-OAuth2Application-properties-description-properties-description-0)

  Title: `Description`
- [id:
  integer](#request-bodyparam-definitions-OAuth2Application-properties-id-properties-id-0)

  Title: `Id`

  Read Only: `true`
- [modified:
  string](#request-bodyparam-definitions-OAuth2Application-properties-modified-properties-modified-0)

  Title: `Modified`

  Read Only: `true`
- [name(required):
  string](#request-bodyparam-definitions-OAuth2Application-properties-name-properties-name-0)

  Title: `Name`

  Maximum Length: `255`
- [organization(required):
  integer](#request-bodyparam-definitions-OAuth2Application-properties-organization-properties-organization-0)

  Title: `Organization`

  Organization containing this application.
- [redirect\_uris:
  string](#request-bodyparam-definitions-OAuth2Application-properties-redirect_uris-properties-redirect_uris-0)

  Title: `Redirect URIs`

  Allowed URIs list, space separated
- [related:
  string](#request-bodyparam-definitions-OAuth2Application-properties-related-properties-related-0)

  Title: `Related`

  Read Only: `true`
- [skip\_authorization:
  boolean](#request-bodyparam-definitions-OAuth2Application-properties-skip_authorization-properties-skip_authorization-0)

  Title: `Skip Authorization`

  Set True to skip authorization step for completely trusted applications.
- [summary\_fields:
  string](#request-bodyparam-definitions-OAuth2Application-properties-summary_fields-properties-summary_fields-0)

  Title: `Summary fields`

  Read Only: `true`
- [type:
  string](#request-bodyparam-definitions-OAuth2Application-properties-type-properties-type-0)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#request-bodyparam-definitions-OAuth2Application-properties-url-properties-url-0)

  Title: `Url`

  Read Only: `true`

```
{
    "properties":{
        "authorization_grant_type":{
            "description":"The Grant type the user must use for acquire tokens for this application.",
            "enum":[
                "authorization-code",
                "password"
            ],
            "title":"Authorization Grant Type",
            "type":"string",
            "x-nullable":true
        },
        "client_id":{
            "minLength":"1",
            "readOnly":true,
            "title":"Client id",
            "type":"string",
            "x-nullable":true
        },
        "client_secret":{
            "description":"Used for more stringent verification of access to an application when creating a token.",
            "minLength":"1",
            "readOnly":true,
            "title":"Client Secret",
            "type":"string",
            "x-nullable":true
        },
        "client_type":{
            "description":"Set to Public or Confidential depending on how secure the client device is.",
            "enum":[
                "confidential",
                "public"
            ],
            "title":"Client Type",
            "type":"string",
            "x-nullable":true
        },
        "created":{
            "readOnly":true,
            "title":"Created",
            "type":"string"
        },
        "description":{
            "title":"Description",
            "type":"string",
            "x-nullable":true
        },
        "id":{
            "readOnly":true,
            "title":"Id",
            "type":"integer"
        },
        "modified":{
            "readOnly":true,
            "title":"Modified",
            "type":"string"
        },
        "name":{
            "maxLength":"255",
            "title":"Name",
            "type":"string",
            "x-nullable":true
        },
        "organization":{
            "description":"Organization containing this application.",
            "title":"Organization",
            "type":"integer"
        },
        "redirect_uris":{
            "description":"Allowed URIs list, space separated",
            "title":"Redirect URIs",
            "type":"string",
            "x-nullable":true
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "skip_authorization":{
            "description":"Set True to skip authorization step for completely trusted applications.",
            "title":"Skip Authorization",
            "type":"boolean",
            "x-nullable":true
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        }
    },
    "required":[
        "name",
        "client_type",
        "authorization_grant_type",
        "organization"
    ],
    "type":"object"
}
```

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

Body ()

Root Schema : OAuth2Application

Type: `object`

[Show Source](#)

- [authorization\_grant\_type(required):
  string](#201-definitions-OAuth2Application-properties-authorization_grant_type-properties-authorization_grant_type-0)

  Title: `Authorization Grant Type`

  Allowed Values: `[
  "authorization-code",
  "password"
  ]`

  The Grant type the user must use for acquire tokens for this application.
- [client\_id:
  string](#201-definitions-OAuth2Application-properties-client_id-properties-client_id-0)

  Title: `Client id`

  Read Only: `true`

  Minimum Length: `1`
- [client\_secret:
  string](#201-definitions-OAuth2Application-properties-client_secret-properties-client_secret-0)

  Title: `Client Secret`

  Read Only: `true`

  Minimum Length: `1`

  Used for more stringent verification of access to an application when creating a token.
- [client\_type(required):
  string](#201-definitions-OAuth2Application-properties-client_type-properties-client_type-0)

  Title: `Client Type`

  Allowed Values: `[
  "confidential",
  "public"
  ]`

  Set to Public or Confidential depending on how secure the client device is.
- [created:
  string](#201-definitions-OAuth2Application-properties-created-properties-created-0)

  Title: `Created`

  Read Only: `true`
- [description:
  string](#201-definitions-OAuth2Application-properties-description-properties-description-0)

  Title: `Description`
- [id:
  integer](#201-definitions-OAuth2Application-properties-id-properties-id-0)

  Title: `Id`

  Read Only: `true`
- [modified:
  string](#201-definitions-OAuth2Application-properties-modified-properties-modified-0)

  Title: `Modified`

  Read Only: `true`
- [name(required):
  string](#201-definitions-OAuth2Application-properties-name-properties-name-0)

  Title: `Name`

  Maximum Length: `255`
- [organization(required):
  integer](#201-definitions-OAuth2Application-properties-organization-properties-organization-0)

  Title: `Organization`

  Organization containing this application.
- [redirect\_uris:
  string](#201-definitions-OAuth2Application-properties-redirect_uris-properties-redirect_uris-0)

  Title: `Redirect URIs`

  Allowed URIs list, space separated
- [related:
  string](#201-definitions-OAuth2Application-properties-related-properties-related-0)

  Title: `Related`

  Read Only: `true`
- [skip\_authorization:
  boolean](#201-definitions-OAuth2Application-properties-skip_authorization-properties-skip_authorization-0)

  Title: `Skip Authorization`

  Set True to skip authorization step for completely trusted applications.
- [summary\_fields:
  string](#201-definitions-OAuth2Application-properties-summary_fields-properties-summary_fields-0)

  Title: `Summary fields`

  Read Only: `true`
- [type:
  string](#201-definitions-OAuth2Application-properties-type-properties-type-0)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#201-definitions-OAuth2Application-properties-url-properties-url-0)

  Title: `Url`

  Read Only: `true`

```
{
    "properties":{
        "authorization_grant_type":{
            "description":"The Grant type the user must use for acquire tokens for this application.",
            "enum":[
                "authorization-code",
                "password"
            ],
            "title":"Authorization Grant Type",
            "type":"string",
            "x-nullable":true
        },
        "client_id":{
            "minLength":"1",
            "readOnly":true,
            "title":"Client id",
            "type":"string",
            "x-nullable":true
        },
        "client_secret":{
            "description":"Used for more stringent verification of access to an application when creating a token.",
            "minLength":"1",
            "readOnly":true,
            "title":"Client Secret",
            "type":"string",
            "x-nullable":true
        },
        "client_type":{
            "description":"Set to Public or Confidential depending on how secure the client device is.",
            "enum":[
                "confidential",
                "public"
            ],
            "title":"Client Type",
            "type":"string",
            "x-nullable":true
        },
        "created":{
            "readOnly":true,
            "title":"Created",
            "type":"string"
        },
        "description":{
            "title":"Description",
            "type":"string",
            "x-nullable":true
        },
        "id":{
            "readOnly":true,
            "title":"Id",
            "type":"integer"
        },
        "modified":{
            "readOnly":true,
            "title":"Modified",
            "type":"string"
        },
        "name":{
            "maxLength":"255",
            "title":"Name",
            "type":"string",
            "x-nullable":true
        },
        "organization":{
            "description":"Organization containing this application.",
            "title":"Organization",
            "type":"integer"
        },
        "redirect_uris":{
            "description":"Allowed URIs list, space separated",
            "title":"Redirect URIs",
            "type":"string",
            "x-nullable":true
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "skip_authorization":{
            "description":"Set True to skip authorization step for completely trusted applications.",
            "title":"Skip Authorization",
            "type":"boolean",
            "x-nullable":true
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        }
    },
    "required":[
        "name",
        "client_type",
        "authorization_grant_type",
        "organization"
    ],
    "type":"object"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-applications-id-delete.html -->

Make a DELETE request to this resource to delete this application.

### Request

Supported Media Types

- application/json

Path Parameters

- [id(required): string](#request-path-param-0)

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 204 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-applications-id-tokens-get.html -->

Make a GET request to this resource to retrieve a list of
access tokens associated with the selected
application.

The resulting data structure contains:

```
{
    "count": 99,
    "next": null,
    "previous": null,
    "results": [
        ...
    ]
}
```

The `count` field indicates the total number of access tokens
found for the given query. The `next` and `previous` fields provides links to
additional results if there are more than will fit on a single page. The
`results` list contains zero or more access token records.

## Results

Each access token data structure includes the following fields:

- `id`: Database ID for this access token. (integer)
- `type`: Data type for this access token. (choice)
- `url`: URL for this access token. (string)
- `related`: Data structure with URLs of related resources. (object)
- `summary_fields`: Data structure with name/description for related resources. The output for some objects may be limited for performance reasons. (object)
- `created`: Timestamp when this access token was created. (datetime)
- `modified`: Timestamp when this access token was last modified. (datetime)
- `description`: Optional description of this access token. (string)
- `user`: The user representing the token owner (id)
- `token`: (string)
- `refresh_token`: (field)
- `application`: (id)
- `expires`: (datetime)
- `scope`: Allowed scopes, further restricts user's permissions. Must be a simple space-separated string with allowed scopes ['read', 'write']. (string)

## Sorting

To specify that access tokens are returned in a particular
order, use the `order_by` query string parameter on the GET request.

```
?order_by=name
```

Prefix the field name with a dash `-` to sort in reverse:

```
?order_by=-name
```

Multiple sorting fields may be specified by separating the field names with a
comma `,`:

```
?order_by=name,some_other_field
```

## Pagination

Use the `page_size` query string parameter to change the number of results
returned for each request. Use the `page` query string parameter to retrieve
a particular page of results.

```
?page_size=100&page=2
```

The `previous` and `next` links returned with the results will set these query
string parameters automatically.

## Searching

Use the `search` query string parameter to perform a case-insensitive search
within all designated text fields of a model.

```
?search=findme
```

(*Added in Ansible Tower 3.1.0*) Search across related fields:

```
?related__search=findme
```

### Request

Supported Media Types

- application/json

Path Parameters

- [id(required): string](#request-path-param-0)

Query Parameters

- [page: integer](#request-query-param-0)

  A page number within the paginated result set.
- [page\_size: integer](#request-query-param-1)

  Number of results to return per page.
- [search: string](#request-query-param-2)

  A search term.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

Body ()

Root Schema : schema

Type: `object`

[Show Source](#)

- [count(required):
  integer](#200-paths--api-v2-applications-{id}-tokens--get-responses-200-schema-properties-count-properties-count-0)
- [next:
  string(uri)](#200-paths--api-v2-applications-{id}-tokens--get-responses-200-schema-properties-next-properties-next-0)
- [previous:
  string(uri)](#200-paths--api-v2-applications-{id}-tokens--get-responses-200-schema-properties-previous-properties-previous-0)
- [results(required):
  array](#200-paths--api-v2-applications-{id}-tokens--get-responses-200-schema-properties-results-properties-results-0)  [results](#200-paths--api-v2-applications-{id}-tokens--get-responses-200-schema-properties-results)

```
{
    "properties":{
        "count":{
            "type":"integer"
        },
        "next":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "previous":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "results":{
            "items":{
                "$ref":"#/definitions/OAuth2Token"
            },
            "type":"array"
        }
    },
    "required":[
        "count",
        "results"
    ],
    "type":"object"
}
```

Nested Schema : results

Type: `array`

[Show Source](#)

- [Array of:
  object](#200-definitions-OAuth2Token-items-0)  [OAuth2Token](#200-definitions-OAuth2Token)

```
{
    "items":{
        "$ref":"#/definitions/OAuth2Token"
    },
    "type":"array"
}
```

Nested Schema : OAuth2Token

Type: `object`

[Show Source](#)

- [application:
  integer](#200-definitions-OAuth2Token-properties-application-properties-application-0)

  Title: `Application`
- [created:
  string](#200-definitions-OAuth2Token-properties-created-properties-created-0)

  Title: `Created`

  Read Only: `true`
- [description:
  string](#200-definitions-OAuth2Token-properties-description-properties-description-0)

  Title: `Description`
- [expires:
  string(date-time)](#200-definitions-OAuth2Token-properties-expires-properties-expires-0)

  Title: `Expires`

  Read Only: `true`
- [id:
  integer](#200-definitions-OAuth2Token-properties-id-properties-id-0)

  Title: `Id`

  Read Only: `true`
- [modified:
  string](#200-definitions-OAuth2Token-properties-modified-properties-modified-0)

  Title: `Modified`

  Read Only: `true`
- [refresh\_token:
  string](#200-definitions-OAuth2Token-properties-refresh_token-properties-refresh_token-0)

  Title: `Refresh token`

  Read Only: `true`
- [related:
  string](#200-definitions-OAuth2Token-properties-related-properties-related-0)

  Title: `Related`

  Read Only: `true`
- [scope:
  string](#200-definitions-OAuth2Token-properties-scope-properties-scope-0)

  Title: `Scope`

  Default Value: `write`

  Allowed scopes, further restricts user's permissions. Must be a simple space-separated string with allowed scopes ['read', 'write'].
- [summary\_fields:
  string](#200-definitions-OAuth2Token-properties-summary_fields-properties-summary_fields-0)

  Title: `Summary fields`

  Read Only: `true`
- [token:
  string](#200-definitions-OAuth2Token-properties-token-properties-token-0)

  Title: `Token`

  Read Only: `true`
- [type:
  string](#200-definitions-OAuth2Token-properties-type-properties-type-0)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#200-definitions-OAuth2Token-properties-url-properties-url-0)

  Title: `Url`

  Read Only: `true`
- [user:
  integer](#200-definitions-OAuth2Token-properties-user-properties-user-0)

  Title: `User`

  Read Only: `true`

  The user representing the token owner

```
{
    "properties":{
        "application":{
            "title":"Application",
            "type":"integer",
            "x-nullable":true
        },
        "created":{
            "readOnly":true,
            "title":"Created",
            "type":"string"
        },
        "description":{
            "title":"Description",
            "type":"string",
            "x-nullable":true
        },
        "expires":{
            "format":"date-time",
            "readOnly":true,
            "title":"Expires",
            "type":"string"
        },
        "id":{
            "readOnly":true,
            "title":"Id",
            "type":"integer"
        },
        "modified":{
            "readOnly":true,
            "title":"Modified",
            "type":"string"
        },
        "refresh_token":{
            "readOnly":true,
            "title":"Refresh token",
            "type":"string"
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "scope":{
            "default":"write",
            "description":"Allowed scopes, further restricts user's permissions. Must be a simple space-separated string with allowed scopes ['read', 'write'].",
            "title":"Scope",
            "type":"string",
            "x-nullable":true
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "token":{
            "readOnly":true,
            "title":"Token",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        },
        "user":{
            "description":"The user representing the token owner",
            "readOnly":true,
            "title":"User",
            "type":"integer"
        }
    },
    "type":"object"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-applications-id-activity_stream-get.html -->

Make a GET request to this resource to retrieve a list of
activity streams associated with the selected
application.

The resulting data structure contains:

```
{
    "count": 99,
    "next": null,
    "previous": null,
    "results": [
        ...
    ]
}
```

The `count` field indicates the total number of activity streams
found for the given query. The `next` and `previous` fields provides links to
additional results if there are more than will fit on a single page. The
`results` list contains zero or more activity stream records.

## Results

Each activity stream data structure includes the following fields:

- `id`: Database ID for this activity stream. (integer)
- `type`: Data type for this activity stream. (choice)
- `url`: URL for this activity stream. (string)
- `related`: Data structure with URLs of related resources. (object)
- `summary_fields`: Data structure with name/description for related resources. The output for some objects may be limited for performance reasons. (object)
- `timestamp`: (datetime)
- `operation`: The action taken with respect to the given object(s). (choice)
  - `create`: Entity Created
  - `update`: Entity Updated
  - `delete`: Entity Deleted
  - `associate`: Entity Associated with another Entity
  - `disassociate`: Entity was Disassociated with another Entity
- `changes`: A summary of the new and changed values when an object is created, updated, or deleted (json)
- `object1`: For create, update, and delete events this is the object type that was affected. For associate and disassociate events this is the object type associated or disassociated with object2. (string)
- `object2`: Unpopulated for create, update, and delete events. For associate and disassociate events this is the object type that object1 is being associated with. (string)
- `object_association`: When present, shows the field name of the role or relationship that changed. (field)
- `action_node`: The cluster node the activity took place on. (string)
- `object_type`: When present, shows the model on which the role or relationship was defined. (field)

## Sorting

To specify that activity streams are returned in a particular
order, use the `order_by` query string parameter on the GET request.

```
?order_by=name
```

Prefix the field name with a dash `-` to sort in reverse:

```
?order_by=-name
```

Multiple sorting fields may be specified by separating the field names with a
comma `,`:

```
?order_by=name,some_other_field
```

## Pagination

Use the `page_size` query string parameter to change the number of results
returned for each request. Use the `page` query string parameter to retrieve
a particular page of results.

```
?page_size=100&page=2
```

The `previous` and `next` links returned with the results will set these query
string parameters automatically.

## Searching

Use the `search` query string parameter to perform a case-insensitive search
within all designated text fields of a model.

```
?search=findme
```

(*Added in Ansible Tower 3.1.0*) Search across related fields:

```
?related__search=findme
```

### Request

Supported Media Types

- application/json

Path Parameters

- [id(required): string](#request-path-param-0)

Query Parameters

- [page: integer](#request-query-param-0)

  A page number within the paginated result set.
- [page\_size: integer](#request-query-param-1)

  Number of results to return per page.
- [search: string](#request-query-param-2)

  A search term.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

Body ()

Root Schema : schema

Type: `object`

[Show Source](#)

- [count(required):
  integer](#200-paths--api-v2-applications-{id}-activity_stream--get-responses-200-schema-properties-count-properties-count-0)
- [next:
  string(uri)](#200-paths--api-v2-applications-{id}-activity_stream--get-responses-200-schema-properties-next-properties-next-0)
- [previous:
  string(uri)](#200-paths--api-v2-applications-{id}-activity_stream--get-responses-200-schema-properties-previous-properties-previous-0)
- [results(required):
  array](#200-paths--api-v2-applications-{id}-activity_stream--get-responses-200-schema-properties-results-properties-results-0)  [results](#200-paths--api-v2-applications-{id}-activity_stream--get-responses-200-schema-properties-results)

```
{
    "properties":{
        "count":{
            "type":"integer"
        },
        "next":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "previous":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "results":{
            "items":{
                "$ref":"#/definitions/ActivityStream"
            },
            "type":"array"
        }
    },
    "required":[
        "count",
        "results"
    ],
    "type":"object"
}
```

Nested Schema : results

Type: `array`

[Show Source](#)

- [Array of:
  object](#200-definitions-ActivityStream-items-0)  [ActivityStream](#200-definitions-ActivityStream)

```
{
    "items":{
        "$ref":"#/definitions/ActivityStream"
    },
    "type":"array"
}
```

Nested Schema : ActivityStream

Type: `object`

[Show Source](#)

- [action\_node:
  string](#200-definitions-ActivityStream-properties-action_node-properties-action_node-3)

  Title: `Action node`

  Read Only: `true`

  Minimum Length: `1`

  The cluster node the activity took place on.
- [changes:
  string](#200-definitions-ActivityStream-properties-changes-properties-changes-3)

  Title: `Changes`

  Read Only: `true`

  A summary of the new and changed values when an object is created, updated, or deleted
- [id:
  integer](#200-definitions-ActivityStream-properties-id-properties-id-3)

  Title: `ID`

  Read Only: `true`
- [object1(required):
  string](#200-definitions-ActivityStream-properties-object1-properties-object1-3)

  Title: `Object1`

  Minimum Length: `1`

  For create, update, and delete events this is the object type that was affected. For associate and disassociate events this is the object type associated or disassociated with object2.
- [object2(required):
  string](#200-definitions-ActivityStream-properties-object2-properties-object2-3)

  Title: `Object2`

  Minimum Length: `1`

  Unpopulated for create, update, and delete events. For associate and disassociate events this is the object type that object1 is being associated with.
- [object\_association:
  string](#200-definitions-ActivityStream-properties-object_association-properties-object_association-3)

  Title: `Object association`

  Read Only: `true`

  When present, shows the field name of the role or relationship that changed.
- [object\_type:
  string](#200-definitions-ActivityStream-properties-object_type-properties-object_type-3)

  Title: `Object type`

  Read Only: `true`

  When present, shows the model on which the role or relationship was defined.
- [operation(required):
  string](#200-definitions-ActivityStream-properties-operation-properties-operation-3)

  Title: `Operation`

  Allowed Values: `[
  "create",
  "update",
  "delete",
  "associate",
  "disassociate"
  ]`

  The action taken with respect to the given object(s).
- [related:
  string](#200-definitions-ActivityStream-properties-related-properties-related-3)

  Title: `Related`

  Read Only: `true`
- [summary\_fields:
  string](#200-definitions-ActivityStream-properties-summary_fields-properties-summary_fields-3)

  Title: `Summary fields`

  Read Only: `true`
- [timestamp:
  string(date-time)](#200-definitions-ActivityStream-properties-timestamp-properties-timestamp-3)

  Title: `Timestamp`

  Read Only: `true`
- [type:
  string](#200-definitions-ActivityStream-properties-type-properties-type-3)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#200-definitions-ActivityStream-properties-url-properties-url-3)

  Title: `Url`

  Read Only: `true`

```
{
    "properties":{
        "action_node":{
            "description":"The cluster node the activity took place on.",
            "minLength":"1",
            "readOnly":true,
            "title":"Action node",
            "type":"string"
        },
        "changes":{
            "description":"A summary of the new and changed values when an object is created, updated, or deleted",
            "readOnly":true,
            "title":"Changes",
            "type":"string"
        },
        "id":{
            "readOnly":true,
            "title":"ID",
            "type":"integer"
        },
        "object1":{
            "description":"For create, update, and delete events this is the object type that was affected. For associate and disassociate events this is the object type associated or disassociated with object2.",
            "minLength":"1",
            "title":"Object1",
            "type":"string",
            "x-nullable":true
        },
        "object2":{
            "description":"Unpopulated for create, update, and delete events. For associate and disassociate events this is the object type that object1 is being associated with.",
            "minLength":"1",
            "title":"Object2",
            "type":"string",
            "x-nullable":true
        },
        "object_association":{
            "description":"When present, shows the field name of the role or relationship that changed.",
            "readOnly":true,
            "title":"Object association",
            "type":"string"
        },
        "object_type":{
            "description":"When present, shows the model on which the role or relationship was defined.",
            "readOnly":true,
            "title":"Object type",
            "type":"string"
        },
        "operation":{
            "description":"The action taken with respect to the given object(s).",
            "enum":[
                "create",
                "update",
                "delete",
                "associate",
                "disassociate"
            ],
            "title":"Operation",
            "type":"string",
            "x-nullable":true
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "timestamp":{
            "format":"date-time",
            "readOnly":true,
            "title":"Timestamp",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        }
    },
    "required":[
        "operation",
        "object1",
        "object2"
    ],
    "type":"object"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-applications-get.html -->

Make a GET request to this resource to retrieve the list of
applications.

The resulting data structure contains:

```
{
    "count": 99,
    "next": null,
    "previous": null,
    "results": [
        ...
    ]
}
```

The `count` field indicates the total number of applications
found for the given query. The `next` and `previous` fields provides links to
additional results if there are more than will fit on a single page. The
`results` list contains zero or more application records.

## Results

Each application data structure includes the following fields:

- `id`: Database ID for this application. (integer)
- `type`: Data type for this application. (choice)
- `url`: URL for this application. (string)
- `related`: Data structure with URLs of related resources. (object)
- `summary_fields`: Data structure with name/description for related resources. The output for some objects may be limited for performance reasons. (object)
- `created`: Timestamp when this application was created. (datetime)
- `modified`: Timestamp when this application was last modified. (datetime)
- `name`: Name of this application. (string)
- `description`: Optional description of this application. (string)
- `client_id`: (string)
- `client_secret`: Used for more stringent verification of access to an application when creating a token. (string)
- `client_type`: Set to Public or Confidential depending on how secure the client device is. (choice)
  - `confidential`: Confidential
  - `public`: Public
- `redirect_uris`: Allowed URIs list, space separated (string)
- `authorization_grant_type`: The Grant type the user must use for acquire tokens for this application. (choice)
  - `authorization-code`: Authorization code
  - `password`: Resource owner password-based
- `skip_authorization`: Set True to skip authorization step for completely trusted applications. (boolean)
- `organization`: Organization containing this application. (id)

## Sorting

To specify that applications are returned in a particular
order, use the `order_by` query string parameter on the GET request.

```
?order_by=name
```

Prefix the field name with a dash `-` to sort in reverse:

```
?order_by=-name
```

Multiple sorting fields may be specified by separating the field names with a
comma `,`:

```
?order_by=name,some_other_field
```

## Pagination

Use the `page_size` query string parameter to change the number of results
returned for each request. Use the `page` query string parameter to retrieve
a particular page of results.

```
?page_size=100&page=2
```

The `previous` and `next` links returned with the results will set these query
string parameters automatically.

## Searching

Use the `search` query string parameter to perform a case-insensitive search
within all designated text fields of a model.

```
?search=findme
```

(*Added in Ansible Tower 3.1.0*) Search across related fields:

```
?related__search=findme
```

### Request

Supported Media Types

- application/json

Query Parameters

- [page: integer](#request-query-param-0)

  A page number within the paginated result set.
- [page\_size: integer](#request-query-param-1)

  Number of results to return per page.
- [search: string](#request-query-param-2)

  A search term.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

Body ()

Root Schema : schema

Type: `object`

[Show Source](#)

- [count(required):
  integer](#200-paths--api-v2-applications--get-responses-200-schema-properties-count-properties-count-0)
- [next:
  string(uri)](#200-paths--api-v2-applications--get-responses-200-schema-properties-next-properties-next-0)
- [previous:
  string(uri)](#200-paths--api-v2-applications--get-responses-200-schema-properties-previous-properties-previous-0)
- [results(required):
  array](#200-paths--api-v2-applications--get-responses-200-schema-properties-results-properties-results-0)  [results](#200-paths--api-v2-applications--get-responses-200-schema-properties-results)

```
{
    "properties":{
        "count":{
            "type":"integer"
        },
        "next":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "previous":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "results":{
            "items":{
                "$ref":"#/definitions/OAuth2Application"
            },
            "type":"array"
        }
    },
    "required":[
        "count",
        "results"
    ],
    "type":"object"
}
```

Nested Schema : results

Type: `array`

[Show Source](#)

- [Array of:
  object](#200-definitions-OAuth2Application-items-0)  [OAuth2Application](#200-definitions-OAuth2Application)

```
{
    "items":{
        "$ref":"#/definitions/OAuth2Application"
    },
    "type":"array"
}
```

Nested Schema : OAuth2Application

Type: `object`

[Show Source](#)

- [authorization\_grant\_type(required):
  string](#200-definitions-OAuth2Application-properties-authorization_grant_type-properties-authorization_grant_type-0)

  Title: `Authorization Grant Type`

  Allowed Values: `[
  "authorization-code",
  "password"
  ]`

  The Grant type the user must use for acquire tokens for this application.
- [client\_id:
  string](#200-definitions-OAuth2Application-properties-client_id-properties-client_id-0)

  Title: `Client id`

  Read Only: `true`

  Minimum Length: `1`
- [client\_secret:
  string](#200-definitions-OAuth2Application-properties-client_secret-properties-client_secret-0)

  Title: `Client Secret`

  Read Only: `true`

  Minimum Length: `1`

  Used for more stringent verification of access to an application when creating a token.
- [client\_type(required):
  string](#200-definitions-OAuth2Application-properties-client_type-properties-client_type-0)

  Title: `Client Type`

  Allowed Values: `[
  "confidential",
  "public"
  ]`

  Set to Public or Confidential depending on how secure the client device is.
- [created:
  string](#200-definitions-OAuth2Application-properties-created-properties-created-0)

  Title: `Created`

  Read Only: `true`
- [description:
  string](#200-definitions-OAuth2Application-properties-description-properties-description-0)

  Title: `Description`
- [id:
  integer](#200-definitions-OAuth2Application-properties-id-properties-id-0)

  Title: `Id`

  Read Only: `true`
- [modified:
  string](#200-definitions-OAuth2Application-properties-modified-properties-modified-0)

  Title: `Modified`

  Read Only: `true`
- [name(required):
  string](#200-definitions-OAuth2Application-properties-name-properties-name-0)

  Title: `Name`

  Maximum Length: `255`
- [organization(required):
  integer](#200-definitions-OAuth2Application-properties-organization-properties-organization-0)

  Title: `Organization`

  Organization containing this application.
- [redirect\_uris:
  string](#200-definitions-OAuth2Application-properties-redirect_uris-properties-redirect_uris-0)

  Title: `Redirect URIs`

  Allowed URIs list, space separated
- [related:
  string](#200-definitions-OAuth2Application-properties-related-properties-related-0)

  Title: `Related`

  Read Only: `true`
- [skip\_authorization:
  boolean](#200-definitions-OAuth2Application-properties-skip_authorization-properties-skip_authorization-0)

  Title: `Skip Authorization`

  Set True to skip authorization step for completely trusted applications.
- [summary\_fields:
  string](#200-definitions-OAuth2Application-properties-summary_fields-properties-summary_fields-0)

  Title: `Summary fields`

  Read Only: `true`
- [type:
  string](#200-definitions-OAuth2Application-properties-type-properties-type-0)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#200-definitions-OAuth2Application-properties-url-properties-url-0)

  Title: `Url`

  Read Only: `true`

```
{
    "properties":{
        "authorization_grant_type":{
            "description":"The Grant type the user must use for acquire tokens for this application.",
            "enum":[
                "authorization-code",
                "password"
            ],
            "title":"Authorization Grant Type",
            "type":"string",
            "x-nullable":true
        },
        "client_id":{
            "minLength":"1",
            "readOnly":true,
            "title":"Client id",
            "type":"string",
            "x-nullable":true
        },
        "client_secret":{
            "description":"Used for more stringent verification of access to an application when creating a token.",
            "minLength":"1",
            "readOnly":true,
            "title":"Client Secret",
            "type":"string",
            "x-nullable":true
        },
        "client_type":{
            "description":"Set to Public or Confidential depending on how secure the client device is.",
            "enum":[
                "confidential",
                "public"
            ],
            "title":"Client Type",
            "type":"string",
            "x-nullable":true
        },
        "created":{
            "readOnly":true,
            "title":"Created",
            "type":"string"
        },
        "description":{
            "title":"Description",
            "type":"string",
            "x-nullable":true
        },
        "id":{
            "readOnly":true,
            "title":"Id",
            "type":"integer"
        },
        "modified":{
            "readOnly":true,
            "title":"Modified",
            "type":"string"
        },
        "name":{
            "maxLength":"255",
            "title":"Name",
            "type":"string",
            "x-nullable":true
        },
        "organization":{
            "description":"Organization containing this application.",
            "title":"Organization",
            "type":"integer"
        },
        "redirect_uris":{
            "description":"Allowed URIs list, space separated",
            "title":"Redirect URIs",
            "type":"string",
            "x-nullable":true
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "skip_authorization":{
            "description":"Set True to skip authorization step for completely trusted applications.",
            "title":"Skip Authorization",
            "type":"boolean",
            "x-nullable":true
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        }
    },
    "required":[
        "name",
        "client_type",
        "authorization_grant_type",
        "organization"
    ],
    "type":"object"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-applications-id-get.html -->

Make GET request to this resource to retrieve a single application
record containing the following fields:

- `id`: Database ID for this application. (integer)
- `type`: Data type for this application. (choice)
- `url`: URL for this application. (string)
- `related`: Data structure with URLs of related resources. (object)
- `summary_fields`: Data structure with name/description for related resources. The output for some objects may be limited for performance reasons. (object)
- `created`: Timestamp when this application was created. (datetime)
- `modified`: Timestamp when this application was last modified. (datetime)
- `name`: Name of this application. (string)
- `description`: Optional description of this application. (string)
- `client_id`: (string)
- `client_secret`: Used for more stringent verification of access to an application when creating a token. (string)
- `client_type`: Set to Public or Confidential depending on how secure the client device is. (choice)
  - `confidential`: Confidential
  - `public`: Public
- `redirect_uris`: Allowed URIs list, space separated (string)
- `authorization_grant_type`: The Grant type the user must use for acquire tokens for this application. (choice)
  - `authorization-code`: Authorization code
  - `password`: Resource owner password-based
- `skip_authorization`: Set True to skip authorization step for completely trusted applications. (boolean)
- `organization`: Organization containing this application. (id)

### Request

Supported Media Types

- application/json

Path Parameters

- [id(required): string](#request-path-param-0)

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

Body ()

Root Schema : OAuth2Application

Type: `object`

[Show Source](#)

- [authorization\_grant\_type(required):
  string](#200-definitions-OAuth2Application-properties-authorization_grant_type-properties-authorization_grant_type-1)

  Title: `Authorization Grant Type`

  Allowed Values: `[
  "authorization-code",
  "password"
  ]`

  The Grant type the user must use for acquire tokens for this application.
- [client\_id:
  string](#200-definitions-OAuth2Application-properties-client_id-properties-client_id-1)

  Title: `Client id`

  Read Only: `true`

  Minimum Length: `1`
- [client\_secret:
  string](#200-definitions-OAuth2Application-properties-client_secret-properties-client_secret-1)

  Title: `Client Secret`

  Read Only: `true`

  Minimum Length: `1`

  Used for more stringent verification of access to an application when creating a token.
- [client\_type(required):
  string](#200-definitions-OAuth2Application-properties-client_type-properties-client_type-1)

  Title: `Client Type`

  Allowed Values: `[
  "confidential",
  "public"
  ]`

  Set to Public or Confidential depending on how secure the client device is.
- [created:
  string](#200-definitions-OAuth2Application-properties-created-properties-created-1)

  Title: `Created`

  Read Only: `true`
- [description:
  string](#200-definitions-OAuth2Application-properties-description-properties-description-1)

  Title: `Description`
- [id:
  integer](#200-definitions-OAuth2Application-properties-id-properties-id-1)

  Title: `Id`

  Read Only: `true`
- [modified:
  string](#200-definitions-OAuth2Application-properties-modified-properties-modified-1)

  Title: `Modified`

  Read Only: `true`
- [name(required):
  string](#200-definitions-OAuth2Application-properties-name-properties-name-1)

  Title: `Name`

  Maximum Length: `255`
- [organization(required):
  integer](#200-definitions-OAuth2Application-properties-organization-properties-organization-1)

  Title: `Organization`

  Organization containing this application.
- [redirect\_uris:
  string](#200-definitions-OAuth2Application-properties-redirect_uris-properties-redirect_uris-1)

  Title: `Redirect URIs`

  Allowed URIs list, space separated
- [related:
  string](#200-definitions-OAuth2Application-properties-related-properties-related-1)

  Title: `Related`

  Read Only: `true`
- [skip\_authorization:
  boolean](#200-definitions-OAuth2Application-properties-skip_authorization-properties-skip_authorization-1)

  Title: `Skip Authorization`

  Set True to skip authorization step for completely trusted applications.
- [summary\_fields:
  string](#200-definitions-OAuth2Application-properties-summary_fields-properties-summary_fields-1)

  Title: `Summary fields`

  Read Only: `true`
- [type:
  string](#200-definitions-OAuth2Application-properties-type-properties-type-1)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#200-definitions-OAuth2Application-properties-url-properties-url-1)

  Title: `Url`

  Read Only: `true`

```
{
    "properties":{
        "authorization_grant_type":{
            "description":"The Grant type the user must use for acquire tokens for this application.",
            "enum":[
                "authorization-code",
                "password"
            ],
            "title":"Authorization Grant Type",
            "type":"string",
            "x-nullable":true
        },
        "client_id":{
            "minLength":"1",
            "readOnly":true,
            "title":"Client id",
            "type":"string",
            "x-nullable":true
        },
        "client_secret":{
            "description":"Used for more stringent verification of access to an application when creating a token.",
            "minLength":"1",
            "readOnly":true,
            "title":"Client Secret",
            "type":"string",
            "x-nullable":true
        },
        "client_type":{
            "description":"Set to Public or Confidential depending on how secure the client device is.",
            "enum":[
                "confidential",
                "public"
            ],
            "title":"Client Type",
            "type":"string",
            "x-nullable":true
        },
        "created":{
            "readOnly":true,
            "title":"Created",
            "type":"string"
        },
        "description":{
            "title":"Description",
            "type":"string",
            "x-nullable":true
        },
        "id":{
            "readOnly":true,
            "title":"Id",
            "type":"integer"
        },
        "modified":{
            "readOnly":true,
            "title":"Modified",
            "type":"string"
        },
        "name":{
            "maxLength":"255",
            "title":"Name",
            "type":"string",
            "x-nullable":true
        },
        "organization":{
            "description":"Organization containing this application.",
            "title":"Organization",
            "type":"integer"
        },
        "redirect_uris":{
            "description":"Allowed URIs list, space separated",
            "title":"Redirect URIs",
            "type":"string",
            "x-nullable":true
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "skip_authorization":{
            "description":"Set True to skip authorization step for completely trusted applications.",
            "title":"Skip Authorization",
            "type":"boolean",
            "x-nullable":true
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        }
    },
    "required":[
        "name",
        "client_type",
        "authorization_grant_type",
        "organization"
    ],
    "type":"object"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-applications-id-patch.html -->

Make a PUT or PATCH request to this resource to update this
application. The following fields may be modified:

- `name`: Name of this application. (string, required)
- `description`: Optional description of this application. (string, default=`""`)
- `client_type`: Set to Public or Confidential depending on how secure the client device is. (choice, required)

  - `confidential`: Confidential
  - `public`: Public
- `redirect_uris`: Allowed URIs list, space separated (string, default=`""`)
- `authorization_grant_type`: The Grant type the user must use for acquire tokens for this application. (choice, required)
  - `authorization-code`: Authorization code
  - `password`: Resource owner password-based
- `skip_authorization`: Set True to skip authorization step for completely trusted applications. (boolean, default=`False`)
- `organization`: Organization containing this application. (id, required)

For a PATCH request, include only the fields that are being modified.

### Request

Supported Media Types

- application/json

Path Parameters

- [id(required): string](#request-path-param-0)

Body ()

Root Schema : OAuth2Application

Type: `object`

[Show Source](#)

- [authorization\_grant\_type(required):
  string](#request-bodyparam-definitions-OAuth2Application-properties-authorization_grant_type-properties-authorization_grant_type-1)

  Title: `Authorization Grant Type`

  Allowed Values: `[
  "authorization-code",
  "password"
  ]`

  The Grant type the user must use for acquire tokens for this application.
- [client\_id:
  string](#request-bodyparam-definitions-OAuth2Application-properties-client_id-properties-client_id-1)

  Title: `Client id`

  Read Only: `true`

  Minimum Length: `1`
- [client\_secret:
  string](#request-bodyparam-definitions-OAuth2Application-properties-client_secret-properties-client_secret-1)

  Title: `Client Secret`

  Read Only: `true`

  Minimum Length: `1`

  Used for more stringent verification of access to an application when creating a token.
- [client\_type(required):
  string](#request-bodyparam-definitions-OAuth2Application-properties-client_type-properties-client_type-1)

  Title: `Client Type`

  Allowed Values: `[
  "confidential",
  "public"
  ]`

  Set to Public or Confidential depending on how secure the client device is.
- [created:
  string](#request-bodyparam-definitions-OAuth2Application-properties-created-properties-created-1)

  Title: `Created`

  Read Only: `true`
- [description:
  string](#request-bodyparam-definitions-OAuth2Application-properties-description-properties-description-1)

  Title: `Description`
- [id:
  integer](#request-bodyparam-definitions-OAuth2Application-properties-id-properties-id-1)

  Title: `Id`

  Read Only: `true`
- [modified:
  string](#request-bodyparam-definitions-OAuth2Application-properties-modified-properties-modified-1)

  Title: `Modified`

  Read Only: `true`
- [name(required):
  string](#request-bodyparam-definitions-OAuth2Application-properties-name-properties-name-1)

  Title: `Name`

  Maximum Length: `255`
- [organization(required):
  integer](#request-bodyparam-definitions-OAuth2Application-properties-organization-properties-organization-1)

  Title: `Organization`

  Organization containing this application.
- [redirect\_uris:
  string](#request-bodyparam-definitions-OAuth2Application-properties-redirect_uris-properties-redirect_uris-1)

  Title: `Redirect URIs`

  Allowed URIs list, space separated
- [related:
  string](#request-bodyparam-definitions-OAuth2Application-properties-related-properties-related-1)

  Title: `Related`

  Read Only: `true`
- [skip\_authorization:
  boolean](#request-bodyparam-definitions-OAuth2Application-properties-skip_authorization-properties-skip_authorization-1)

  Title: `Skip Authorization`

  Set True to skip authorization step for completely trusted applications.
- [summary\_fields:
  string](#request-bodyparam-definitions-OAuth2Application-properties-summary_fields-properties-summary_fields-1)

  Title: `Summary fields`

  Read Only: `true`
- [type:
  string](#request-bodyparam-definitions-OAuth2Application-properties-type-properties-type-1)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#request-bodyparam-definitions-OAuth2Application-properties-url-properties-url-1)

  Title: `Url`

  Read Only: `true`

```
{
    "properties":{
        "authorization_grant_type":{
            "description":"The Grant type the user must use for acquire tokens for this application.",
            "enum":[
                "authorization-code",
                "password"
            ],
            "title":"Authorization Grant Type",
            "type":"string",
            "x-nullable":true
        },
        "client_id":{
            "minLength":"1",
            "readOnly":true,
            "title":"Client id",
            "type":"string",
            "x-nullable":true
        },
        "client_secret":{
            "description":"Used for more stringent verification of access to an application when creating a token.",
            "minLength":"1",
            "readOnly":true,
            "title":"Client Secret",
            "type":"string",
            "x-nullable":true
        },
        "client_type":{
            "description":"Set to Public or Confidential depending on how secure the client device is.",
            "enum":[
                "confidential",
                "public"
            ],
            "title":"Client Type",
            "type":"string",
            "x-nullable":true
        },
        "created":{
            "readOnly":true,
            "title":"Created",
            "type":"string"
        },
        "description":{
            "title":"Description",
            "type":"string",
            "x-nullable":true
        },
        "id":{
            "readOnly":true,
            "title":"Id",
            "type":"integer"
        },
        "modified":{
            "readOnly":true,
            "title":"Modified",
            "type":"string"
        },
        "name":{
            "maxLength":"255",
            "title":"Name",
            "type":"string",
            "x-nullable":true
        },
        "organization":{
            "description":"Organization containing this application.",
            "title":"Organization",
            "type":"integer"
        },
        "redirect_uris":{
            "description":"Allowed URIs list, space separated",
            "title":"Redirect URIs",
            "type":"string",
            "x-nullable":true
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "skip_authorization":{
            "description":"Set True to skip authorization step for completely trusted applications.",
            "title":"Skip Authorization",
            "type":"boolean",
            "x-nullable":true
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        }
    },
    "required":[
        "name",
        "client_type",
        "authorization_grant_type",
        "organization"
    ],
    "type":"object"
}
```

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

Body ()

Root Schema : OAuth2Application

Type: `object`

[Show Source](#)

- [authorization\_grant\_type(required):
  string](#200-definitions-OAuth2Application-properties-authorization_grant_type-properties-authorization_grant_type-2)

  Title: `Authorization Grant Type`

  Allowed Values: `[
  "authorization-code",
  "password"
  ]`

  The Grant type the user must use for acquire tokens for this application.
- [client\_id:
  string](#200-definitions-OAuth2Application-properties-client_id-properties-client_id-2)

  Title: `Client id`

  Read Only: `true`

  Minimum Length: `1`
- [client\_secret:
  string](#200-definitions-OAuth2Application-properties-client_secret-properties-client_secret-2)

  Title: `Client Secret`

  Read Only: `true`

  Minimum Length: `1`

  Used for more stringent verification of access to an application when creating a token.
- [client\_type(required):
  string](#200-definitions-OAuth2Application-properties-client_type-properties-client_type-2)

  Title: `Client Type`

  Allowed Values: `[
  "confidential",
  "public"
  ]`

  Set to Public or Confidential depending on how secure the client device is.
- [created:
  string](#200-definitions-OAuth2Application-properties-created-properties-created-2)

  Title: `Created`

  Read Only: `true`
- [description:
  string](#200-definitions-OAuth2Application-properties-description-properties-description-2)

  Title: `Description`
- [id:
  integer](#200-definitions-OAuth2Application-properties-id-properties-id-2)

  Title: `Id`

  Read Only: `true`
- [modified:
  string](#200-definitions-OAuth2Application-properties-modified-properties-modified-2)

  Title: `Modified`

  Read Only: `true`
- [name(required):
  string](#200-definitions-OAuth2Application-properties-name-properties-name-2)

  Title: `Name`

  Maximum Length: `255`
- [organization(required):
  integer](#200-definitions-OAuth2Application-properties-organization-properties-organization-2)

  Title: `Organization`

  Organization containing this application.
- [redirect\_uris:
  string](#200-definitions-OAuth2Application-properties-redirect_uris-properties-redirect_uris-2)

  Title: `Redirect URIs`

  Allowed URIs list, space separated
- [related:
  string](#200-definitions-OAuth2Application-properties-related-properties-related-2)

  Title: `Related`

  Read Only: `true`
- [skip\_authorization:
  boolean](#200-definitions-OAuth2Application-properties-skip_authorization-properties-skip_authorization-2)

  Title: `Skip Authorization`

  Set True to skip authorization step for completely trusted applications.
- [summary\_fields:
  string](#200-definitions-OAuth2Application-properties-summary_fields-properties-summary_fields-2)

  Title: `Summary fields`

  Read Only: `true`
- [type:
  string](#200-definitions-OAuth2Application-properties-type-properties-type-2)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#200-definitions-OAuth2Application-properties-url-properties-url-2)

  Title: `Url`

  Read Only: `true`

```
{
    "properties":{
        "authorization_grant_type":{
            "description":"The Grant type the user must use for acquire tokens for this application.",
            "enum":[
                "authorization-code",
                "password"
            ],
            "title":"Authorization Grant Type",
            "type":"string",
            "x-nullable":true
        },
        "client_id":{
            "minLength":"1",
            "readOnly":true,
            "title":"Client id",
            "type":"string",
            "x-nullable":true
        },
        "client_secret":{
            "description":"Used for more stringent verification of access to an application when creating a token.",
            "minLength":"1",
            "readOnly":true,
            "title":"Client Secret",
            "type":"string",
            "x-nullable":true
        },
        "client_type":{
            "description":"Set to Public or Confidential depending on how secure the client device is.",
            "enum":[
                "confidential",
                "public"
            ],
            "title":"Client Type",
            "type":"string",
            "x-nullable":true
        },
        "created":{
            "readOnly":true,
            "title":"Created",
            "type":"string"
        },
        "description":{
            "title":"Description",
            "type":"string",
            "x-nullable":true
        },
        "id":{
            "readOnly":true,
            "title":"Id",
            "type":"integer"
        },
        "modified":{
            "readOnly":true,
            "title":"Modified",
            "type":"string"
        },
        "name":{
            "maxLength":"255",
            "title":"Name",
            "type":"string",
            "x-nullable":true
        },
        "organization":{
            "description":"Organization containing this application.",
            "title":"Organization",
            "type":"integer"
        },
        "redirect_uris":{
            "description":"Allowed URIs list, space separated",
            "title":"Redirect URIs",
            "type":"string",
            "x-nullable":true
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "skip_authorization":{
            "description":"Set True to skip authorization step for completely trusted applications.",
            "title":"Skip Authorization",
            "type":"boolean",
            "x-nullable":true
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        }
    },
    "required":[
        "name",
        "client_type",
        "authorization_grant_type",
        "organization"
    ],
    "type":"object"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-applications-id-put.html -->

Make a PUT or PATCH request to this resource to update this
application. The following fields may be modified:

- `name`: Name of this application. (string, required)
- `description`: Optional description of this application. (string, default=`""`)
- `client_type`: Set to Public or Confidential depending on how secure the client device is. (choice, required)

  - `confidential`: Confidential
  - `public`: Public
- `redirect_uris`: Allowed URIs list, space separated (string, default=`""`)
- `authorization_grant_type`: The Grant type the user must use for acquire tokens for this application. (choice, required)
  - `authorization-code`: Authorization code
  - `password`: Resource owner password-based
- `skip_authorization`: Set True to skip authorization step for completely trusted applications. (boolean, default=`False`)
- `organization`: Organization containing this application. (id, required)

For a PUT request, include **all** fields in the request.

### Request

Supported Media Types

- application/json

Path Parameters

- [id(required): string](#request-path-param-0)

Body ()

Root Schema : OAuth2Application

Type: `object`

[Show Source](#)

- [authorization\_grant\_type(required):
  string](#request-bodyparam-definitions-OAuth2Application-properties-authorization_grant_type-properties-authorization_grant_type-2)

  Title: `Authorization Grant Type`

  Allowed Values: `[
  "authorization-code",
  "password"
  ]`

  The Grant type the user must use for acquire tokens for this application.
- [client\_id:
  string](#request-bodyparam-definitions-OAuth2Application-properties-client_id-properties-client_id-2)

  Title: `Client id`

  Read Only: `true`

  Minimum Length: `1`
- [client\_secret:
  string](#request-bodyparam-definitions-OAuth2Application-properties-client_secret-properties-client_secret-2)

  Title: `Client Secret`

  Read Only: `true`

  Minimum Length: `1`

  Used for more stringent verification of access to an application when creating a token.
- [client\_type(required):
  string](#request-bodyparam-definitions-OAuth2Application-properties-client_type-properties-client_type-2)

  Title: `Client Type`

  Allowed Values: `[
  "confidential",
  "public"
  ]`

  Set to Public or Confidential depending on how secure the client device is.
- [created:
  string](#request-bodyparam-definitions-OAuth2Application-properties-created-properties-created-2)

  Title: `Created`

  Read Only: `true`
- [description:
  string](#request-bodyparam-definitions-OAuth2Application-properties-description-properties-description-2)

  Title: `Description`
- [id:
  integer](#request-bodyparam-definitions-OAuth2Application-properties-id-properties-id-2)

  Title: `Id`

  Read Only: `true`
- [modified:
  string](#request-bodyparam-definitions-OAuth2Application-properties-modified-properties-modified-2)

  Title: `Modified`

  Read Only: `true`
- [name(required):
  string](#request-bodyparam-definitions-OAuth2Application-properties-name-properties-name-2)

  Title: `Name`

  Maximum Length: `255`
- [organization(required):
  integer](#request-bodyparam-definitions-OAuth2Application-properties-organization-properties-organization-2)

  Title: `Organization`

  Organization containing this application.
- [redirect\_uris:
  string](#request-bodyparam-definitions-OAuth2Application-properties-redirect_uris-properties-redirect_uris-2)

  Title: `Redirect URIs`

  Allowed URIs list, space separated
- [related:
  string](#request-bodyparam-definitions-OAuth2Application-properties-related-properties-related-2)

  Title: `Related`

  Read Only: `true`
- [skip\_authorization:
  boolean](#request-bodyparam-definitions-OAuth2Application-properties-skip_authorization-properties-skip_authorization-2)

  Title: `Skip Authorization`

  Set True to skip authorization step for completely trusted applications.
- [summary\_fields:
  string](#request-bodyparam-definitions-OAuth2Application-properties-summary_fields-properties-summary_fields-2)

  Title: `Summary fields`

  Read Only: `true`
- [type:
  string](#request-bodyparam-definitions-OAuth2Application-properties-type-properties-type-2)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#request-bodyparam-definitions-OAuth2Application-properties-url-properties-url-2)

  Title: `Url`

  Read Only: `true`

```
{
    "properties":{
        "authorization_grant_type":{
            "description":"The Grant type the user must use for acquire tokens for this application.",
            "enum":[
                "authorization-code",
                "password"
            ],
            "title":"Authorization Grant Type",
            "type":"string",
            "x-nullable":true
        },
        "client_id":{
            "minLength":"1",
            "readOnly":true,
            "title":"Client id",
            "type":"string",
            "x-nullable":true
        },
        "client_secret":{
            "description":"Used for more stringent verification of access to an application when creating a token.",
            "minLength":"1",
            "readOnly":true,
            "title":"Client Secret",
            "type":"string",
            "x-nullable":true
        },
        "client_type":{
            "description":"Set to Public or Confidential depending on how secure the client device is.",
            "enum":[
                "confidential",
                "public"
            ],
            "title":"Client Type",
            "type":"string",
            "x-nullable":true
        },
        "created":{
            "readOnly":true,
            "title":"Created",
            "type":"string"
        },
        "description":{
            "title":"Description",
            "type":"string",
            "x-nullable":true
        },
        "id":{
            "readOnly":true,
            "title":"Id",
            "type":"integer"
        },
        "modified":{
            "readOnly":true,
            "title":"Modified",
            "type":"string"
        },
        "name":{
            "maxLength":"255",
            "title":"Name",
            "type":"string",
            "x-nullable":true
        },
        "organization":{
            "description":"Organization containing this application.",
            "title":"Organization",
            "type":"integer"
        },
        "redirect_uris":{
            "description":"Allowed URIs list, space separated",
            "title":"Redirect URIs",
            "type":"string",
            "x-nullable":true
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "skip_authorization":{
            "description":"Set True to skip authorization step for completely trusted applications.",
            "title":"Skip Authorization",
            "type":"boolean",
            "x-nullable":true
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        }
    },
    "required":[
        "name",
        "client_type",
        "authorization_grant_type",
        "organization"
    ],
    "type":"object"
}
```

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

Body ()

Root Schema : OAuth2Application

Type: `object`

[Show Source](#)

- [authorization\_grant\_type(required):
  string](#200-definitions-OAuth2Application-properties-authorization_grant_type-properties-authorization_grant_type-3)

  Title: `Authorization Grant Type`

  Allowed Values: `[
  "authorization-code",
  "password"
  ]`

  The Grant type the user must use for acquire tokens for this application.
- [client\_id:
  string](#200-definitions-OAuth2Application-properties-client_id-properties-client_id-3)

  Title: `Client id`

  Read Only: `true`

  Minimum Length: `1`
- [client\_secret:
  string](#200-definitions-OAuth2Application-properties-client_secret-properties-client_secret-3)

  Title: `Client Secret`

  Read Only: `true`

  Minimum Length: `1`

  Used for more stringent verification of access to an application when creating a token.
- [client\_type(required):
  string](#200-definitions-OAuth2Application-properties-client_type-properties-client_type-3)

  Title: `Client Type`

  Allowed Values: `[
  "confidential",
  "public"
  ]`

  Set to Public or Confidential depending on how secure the client device is.
- [created:
  string](#200-definitions-OAuth2Application-properties-created-properties-created-3)

  Title: `Created`

  Read Only: `true`
- [description:
  string](#200-definitions-OAuth2Application-properties-description-properties-description-3)

  Title: `Description`
- [id:
  integer](#200-definitions-OAuth2Application-properties-id-properties-id-3)

  Title: `Id`

  Read Only: `true`
- [modified:
  string](#200-definitions-OAuth2Application-properties-modified-properties-modified-3)

  Title: `Modified`

  Read Only: `true`
- [name(required):
  string](#200-definitions-OAuth2Application-properties-name-properties-name-3)

  Title: `Name`

  Maximum Length: `255`
- [organization(required):
  integer](#200-definitions-OAuth2Application-properties-organization-properties-organization-3)

  Title: `Organization`

  Organization containing this application.
- [redirect\_uris:
  string](#200-definitions-OAuth2Application-properties-redirect_uris-properties-redirect_uris-3)

  Title: `Redirect URIs`

  Allowed URIs list, space separated
- [related:
  string](#200-definitions-OAuth2Application-properties-related-properties-related-3)

  Title: `Related`

  Read Only: `true`
- [skip\_authorization:
  boolean](#200-definitions-OAuth2Application-properties-skip_authorization-properties-skip_authorization-3)

  Title: `Skip Authorization`

  Set True to skip authorization step for completely trusted applications.
- [summary\_fields:
  string](#200-definitions-OAuth2Application-properties-summary_fields-properties-summary_fields-3)

  Title: `Summary fields`

  Read Only: `true`
- [type:
  string](#200-definitions-OAuth2Application-properties-type-properties-type-3)

  Title: `Type`

  Read Only: `true`
- [url:
  string](#200-definitions-OAuth2Application-properties-url-properties-url-3)

  Title: `Url`

  Read Only: `true`

```
{
    "properties":{
        "authorization_grant_type":{
            "description":"The Grant type the user must use for acquire tokens for this application.",
            "enum":[
                "authorization-code",
                "password"
            ],
            "title":"Authorization Grant Type",
            "type":"string",
            "x-nullable":true
        },
        "client_id":{
            "minLength":"1",
            "readOnly":true,
            "title":"Client id",
            "type":"string",
            "x-nullable":true
        },
        "client_secret":{
            "description":"Used for more stringent verification of access to an application when creating a token.",
            "minLength":"1",
            "readOnly":true,
            "title":"Client Secret",
            "type":"string",
            "x-nullable":true
        },
        "client_type":{
            "description":"Set to Public or Confidential depending on how secure the client device is.",
            "enum":[
                "confidential",
                "public"
            ],
            "title":"Client Type",
            "type":"string",
            "x-nullable":true
        },
        "created":{
            "readOnly":true,
            "title":"Created",
            "type":"string"
        },
        "description":{
            "title":"Description",
            "type":"string",
            "x-nullable":true
        },
        "id":{
            "readOnly":true,
            "title":"Id",
            "type":"integer"
        },
        "modified":{
            "readOnly":true,
            "title":"Modified",
            "type":"string"
        },
        "name":{
            "maxLength":"255",
            "title":"Name",
            "type":"string",
            "x-nullable":true
        },
        "organization":{
            "description":"Organization containing this application.",
            "title":"Organization",
            "type":"integer"
        },
        "redirect_uris":{
            "description":"Allowed URIs list, space separated",
            "title":"Redirect URIs",
            "type":"string",
            "x-nullable":true
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "skip_authorization":{
            "description":"Set True to skip authorization step for completely trusted applications.",
            "title":"Skip Authorization",
            "type":"boolean",
            "x-nullable":true
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        }
    },
    "required":[
        "name",
        "client_type",
        "authorization_grant_type",
        "organization"
    ],
    "type":"object"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/api-auth.html -->

Sort by

Task

 Path

 Method

Auth

REST API endpoints for Auth

[Auth List](op-api-v2-auth-get.html)
:   Method: get

    Path: `/api/v2/auth/`


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-auth-get.html -->

List enabled single-sign-on endpoints

### Request

There are no request parameters for this operation.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/api-bulk.html -->

Sort by

Task

 Path

 Method

Bulk

REST API endpoints for Bulk

[Bulk Host Create](op-api-v2-bulk-host_create-get.html)
:   Method: get

    Path: `/api/v2/bulk/host_create/`

[Bulk Host Create](op-api-v2-bulk-host_create-post.html)
:   Method: post

    Path: `/api/v2/bulk/host_create/`

[Bulk Host Delete](op-api-v2-bulk-host_delete-get.html)
:   Method: get

    Path: `/api/v2/bulk/host_delete/`

[Bulk Host Delete](op-api-v2-bulk-host_delete-post.html)
:   Method: post

    Path: `/api/v2/bulk/host_delete/`

[Bulk Job Launch](op-api-v2-bulk-job_launch-get.html)
:   Method: get

    Path: `/api/v2/bulk/job_launch/`

[Bulk Job Launch](op-api-v2-bulk-job_launch-post.html)
:   Method: post

    Path: `/api/v2/bulk/job_launch/`

[Bulk List](op-api-v2-bulk-get.html)
:   Method: get

    Path: `/api/v2/bulk/`


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-bulk-host_create-get.html -->

This endpoint allows the client to create multiple hosts and associate them with an inventory. They may do this by providing the inventory ID and a list of json that would normally be provided to create hosts.

### Request

Supported Media Types

- application/json

Query Parameters

- [page: integer](#request-query-param-0)

  A page number within the paginated result set.
- [page\_size: integer](#request-query-param-1)

  Number of results to return per page.
- [search: string](#request-query-param-2)

  A search term.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

Body ()

Root Schema : schema

Type: `object`

[Show Source](#)

- [count(required):
  integer](#200-paths--api-v2-bulk-host_create--get-responses-200-schema-properties-count-properties-count-0)
- [next:
  string(uri)](#200-paths--api-v2-bulk-host_create--get-responses-200-schema-properties-next-properties-next-0)
- [previous:
  string(uri)](#200-paths--api-v2-bulk-host_create--get-responses-200-schema-properties-previous-properties-previous-0)
- [results(required):
  array](#200-paths--api-v2-bulk-host_create--get-responses-200-schema-properties-results-properties-results-0)  [results](#200-paths--api-v2-bulk-host_create--get-responses-200-schema-properties-results)

```
{
    "properties":{
        "count":{
            "type":"integer"
        },
        "next":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "previous":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "results":{
            "items":{
                "$ref":"#/definitions/BulkHostCreate"
            },
            "type":"array"
        }
    },
    "required":[
        "count",
        "results"
    ],
    "type":"object"
}
```

Nested Schema : results

Type: `array`

[Show Source](#)

- [Array of:
  object](#200-definitions-BulkHostCreate-items-0)  [BulkHostCreate](#200-definitions-BulkHostCreate)

```
{
    "items":{
        "$ref":"#/definitions/BulkHostCreate"
    },
    "type":"array"
}
```

Nested Schema : BulkHostCreate

Type: `object`

[Show Source](#)

- [hosts(required):
  array](#200-definitions-BulkHostCreate-properties-hosts-properties-hosts-0)  [hosts](#200-definitions-BulkHostCreate-properties-hosts)

  Maximum Number of Items: `100000`

  List of hosts to be created, JSON. e.g. [{"name": "example.com"}, {"name": "127.0.0.1"}]
- [inventory(required):
  integer](#200-definitions-BulkHostCreate-properties-inventory-properties-inventory-0)

  Title: `Inventory`

  Primary Key ID of inventory to add hosts to.

```
{
    "properties":{
        "hosts":{
            "description":"List of hosts to be created, JSON. e.g. [{\"name\": \"example.com\"}, {\"name\": \"127.0.0.1\"}]",
            "items":{
                "$ref":"#/definitions/BulkHost"
            },
            "maxItems":"100000",
            "type":"array"
        },
        "inventory":{
            "description":"Primary Key ID of inventory to add hosts to.",
            "title":"Inventory",
            "type":"integer"
        }
    },
    "required":[
        "inventory",
        "hosts"
    ],
    "type":"object"
}
```

Nested Schema : hosts

Type: `array`

Maximum Number of Items: `100000`

List of hosts to be created, JSON. e.g. [{"name": "example.com"}, {"name": "127.0.0.1"}]

[Show Source](#)

- [Array of:
  object](#200-definitions-BulkHost-items-0)  [BulkHost](#200-definitions-BulkHost)

```
{
    "description":"List of hosts to be created, JSON. e.g. [{\"name\": \"example.com\"}, {\"name\": \"127.0.0.1\"}]",
    "items":{
        "$ref":"#/definitions/BulkHost"
    },
    "maxItems":"100000",
    "type":"array"
}
```

Nested Schema : BulkHost

Type: `object`

[Show Source](#)

- [description:
  string](#200-definitions-BulkHost-properties-description-properties-description-0)

  Title: `Description`
- [enabled:
  boolean](#200-definitions-BulkHost-properties-enabled-properties-enabled-0)

  Title: `Enabled`

  Default Value: `true`

  Is this host online and available for running jobs?
- [instance\_id:
  string](#200-definitions-BulkHost-properties-instance_id-properties-instance_id-0)

  Title: `Instance id`

  Maximum Length: `1024`

  The value used by the remote inventory source to uniquely identify the host
- [name(required):
  string](#200-definitions-BulkHost-properties-name-properties-name-0)

  Title: `Name`

  Minimum Length: `1`

  Maximum Length: `512`
- [variables:
  string](#200-definitions-BulkHost-properties-variables-properties-variables-0)

  Title: `Variables`

  Host variables in JSON or YAML format.

```
{
    "properties":{
        "description":{
            "title":"Description",
            "type":"string",
            "x-nullable":true
        },
        "enabled":{
            "default":true,
            "description":"Is this host online and available for running jobs?",
            "title":"Enabled",
            "type":"boolean",
            "x-nullable":true
        },
        "instance_id":{
            "description":"The value used by the remote inventory source to uniquely identify the host",
            "maxLength":"1024",
            "title":"Instance id",
            "type":"string",
            "x-nullable":true
        },
        "name":{
            "maxLength":"512",
            "minLength":"1",
            "title":"Name",
            "type":"string",
            "x-nullable":true
        },
        "variables":{
            "description":"Host variables in JSON or YAML format.",
            "title":"Variables",
            "type":"string",
            "x-nullable":true
        }
    },
    "required":[
        "name"
    ],
    "type":"object"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-bulk-host_create-post.html -->

This endpoint allows the client to create multiple hosts and associate them with an inventory. They may do this by providing the inventory ID and a list of json that would normally be provided to create hosts.

### Request

Supported Media Types

- application/json

Body ()

Root Schema : BulkHostCreate

Type: `object`

[Show Source](#)

- [hosts(required):
  array](#request-bodyparam-definitions-BulkHostCreate-properties-hosts-properties-hosts-0)  [hosts](#request-bodyparam-definitions-BulkHostCreate-properties-hosts)

  Maximum Number of Items: `100000`

  List of hosts to be created, JSON. e.g. [{"name": "example.com"}, {"name": "127.0.0.1"}]
- [inventory(required):
  integer](#request-bodyparam-definitions-BulkHostCreate-properties-inventory-properties-inventory-0)

  Title: `Inventory`

  Primary Key ID of inventory to add hosts to.

```
{
    "properties":{
        "hosts":{
            "description":"List of hosts to be created, JSON. e.g. [{\"name\": \"example.com\"}, {\"name\": \"127.0.0.1\"}]",
            "items":{
                "$ref":"#/definitions/BulkHost"
            },
            "maxItems":"100000",
            "type":"array"
        },
        "inventory":{
            "description":"Primary Key ID of inventory to add hosts to.",
            "title":"Inventory",
            "type":"integer"
        }
    },
    "required":[
        "inventory",
        "hosts"
    ],
    "type":"object"
}
```

Nested Schema : hosts

Type: `array`

Maximum Number of Items: `100000`

List of hosts to be created, JSON. e.g. [{"name": "example.com"}, {"name": "127.0.0.1"}]

[Show Source](#)

- [Array of:
  object](#request-bodyparam-definitions-BulkHost-items-0)  [BulkHost](#request-bodyparam-definitions-BulkHost)

```
{
    "description":"List of hosts to be created, JSON. e.g. [{\"name\": \"example.com\"}, {\"name\": \"127.0.0.1\"}]",
    "items":{
        "$ref":"#/definitions/BulkHost"
    },
    "maxItems":"100000",
    "type":"array"
}
```

Nested Schema : BulkHost

Type: `object`

[Show Source](#)

- [description:
  string](#request-bodyparam-definitions-BulkHost-properties-description-properties-description-0)

  Title: `Description`
- [enabled:
  boolean](#request-bodyparam-definitions-BulkHost-properties-enabled-properties-enabled-0)

  Title: `Enabled`

  Default Value: `true`

  Is this host online and available for running jobs?
- [instance\_id:
  string](#request-bodyparam-definitions-BulkHost-properties-instance_id-properties-instance_id-0)

  Title: `Instance id`

  Maximum Length: `1024`

  The value used by the remote inventory source to uniquely identify the host
- [name(required):
  string](#request-bodyparam-definitions-BulkHost-properties-name-properties-name-0)

  Title: `Name`

  Minimum Length: `1`

  Maximum Length: `512`
- [variables:
  string](#request-bodyparam-definitions-BulkHost-properties-variables-properties-variables-0)

  Title: `Variables`

  Host variables in JSON or YAML format.

```
{
    "properties":{
        "description":{
            "title":"Description",
            "type":"string",
            "x-nullable":true
        },
        "enabled":{
            "default":true,
            "description":"Is this host online and available for running jobs?",
            "title":"Enabled",
            "type":"boolean",
            "x-nullable":true
        },
        "instance_id":{
            "description":"The value used by the remote inventory source to uniquely identify the host",
            "maxLength":"1024",
            "title":"Instance id",
            "type":"string",
            "x-nullable":true
        },
        "name":{
            "maxLength":"512",
            "minLength":"1",
            "title":"Name",
            "type":"string",
            "x-nullable":true
        },
        "variables":{
            "description":"Host variables in JSON or YAML format.",
            "title":"Variables",
            "type":"string",
            "x-nullable":true
        }
    },
    "required":[
        "name"
    ],
    "type":"object"
}
```

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

Body ()

Root Schema : BulkHostCreate

Type: `object`

[Show Source](#)

- [hosts(required):
  array](#201-definitions-BulkHostCreate-properties-hosts-properties-hosts-0)  [hosts](#201-definitions-BulkHostCreate-properties-hosts)

  Maximum Number of Items: `100000`

  List of hosts to be created, JSON. e.g. [{"name": "example.com"}, {"name": "127.0.0.1"}]
- [inventory(required):
  integer](#201-definitions-BulkHostCreate-properties-inventory-properties-inventory-0)

  Title: `Inventory`

  Primary Key ID of inventory to add hosts to.

```
{
    "properties":{
        "hosts":{
            "description":"List of hosts to be created, JSON. e.g. [{\"name\": \"example.com\"}, {\"name\": \"127.0.0.1\"}]",
            "items":{
                "$ref":"#/definitions/BulkHost"
            },
            "maxItems":"100000",
            "type":"array"
        },
        "inventory":{
            "description":"Primary Key ID of inventory to add hosts to.",
            "title":"Inventory",
            "type":"integer"
        }
    },
    "required":[
        "inventory",
        "hosts"
    ],
    "type":"object"
}
```

Nested Schema : hosts

Type: `array`

Maximum Number of Items: `100000`

List of hosts to be created, JSON. e.g. [{"name": "example.com"}, {"name": "127.0.0.1"}]

[Show Source](#)

- [Array of:
  object](#201-definitions-BulkHost-items-0)  [BulkHost](#201-definitions-BulkHost)

```
{
    "description":"List of hosts to be created, JSON. e.g. [{\"name\": \"example.com\"}, {\"name\": \"127.0.0.1\"}]",
    "items":{
        "$ref":"#/definitions/BulkHost"
    },
    "maxItems":"100000",
    "type":"array"
}
```

Nested Schema : BulkHost

Type: `object`

[Show Source](#)

- [description:
  string](#201-definitions-BulkHost-properties-description-properties-description-0)

  Title: `Description`
- [enabled:
  boolean](#201-definitions-BulkHost-properties-enabled-properties-enabled-0)

  Title: `Enabled`

  Default Value: `true`

  Is this host online and available for running jobs?
- [instance\_id:
  string](#201-definitions-BulkHost-properties-instance_id-properties-instance_id-0)

  Title: `Instance id`

  Maximum Length: `1024`

  The value used by the remote inventory source to uniquely identify the host
- [name(required):
  string](#201-definitions-BulkHost-properties-name-properties-name-0)

  Title: `Name`

  Minimum Length: `1`

  Maximum Length: `512`
- [variables:
  string](#201-definitions-BulkHost-properties-variables-properties-variables-0)

  Title: `Variables`

  Host variables in JSON or YAML format.

```
{
    "properties":{
        "description":{
            "title":"Description",
            "type":"string",
            "x-nullable":true
        },
        "enabled":{
            "default":true,
            "description":"Is this host online and available for running jobs?",
            "title":"Enabled",
            "type":"boolean",
            "x-nullable":true
        },
        "instance_id":{
            "description":"The value used by the remote inventory source to uniquely identify the host",
            "maxLength":"1024",
            "title":"Instance id",
            "type":"string",
            "x-nullable":true
        },
        "name":{
            "maxLength":"512",
            "minLength":"1",
            "title":"Name",
            "type":"string",
            "x-nullable":true
        },
        "variables":{
            "description":"Host variables in JSON or YAML format.",
            "title":"Variables",
            "type":"string",
            "x-nullable":true
        }
    },
    "required":[
        "name"
    ],
    "type":"object"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-bulk-host_delete-get.html -->

This endpoint allows the client to delete multiple hosts from inventories.
They may do this by providing a list of hosts ID's to be deleted.

### Request

Supported Media Types

- application/json

Query Parameters

- [page: integer](#request-query-param-0)

  A page number within the paginated result set.
- [page\_size: integer](#request-query-param-1)

  Number of results to return per page.
- [search: string](#request-query-param-2)

  A search term.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

Body ()

Root Schema : schema

Type: `object`

[Show Source](#)

- [count(required):
  integer](#200-paths--api-v2-bulk-host_delete--get-responses-200-schema-properties-count-properties-count-0)
- [next:
  string(uri)](#200-paths--api-v2-bulk-host_delete--get-responses-200-schema-properties-next-properties-next-0)
- [previous:
  string(uri)](#200-paths--api-v2-bulk-host_delete--get-responses-200-schema-properties-previous-properties-previous-0)
- [results(required):
  array](#200-paths--api-v2-bulk-host_delete--get-responses-200-schema-properties-results-properties-results-0)  [results](#200-paths--api-v2-bulk-host_delete--get-responses-200-schema-properties-results)

```
{
    "properties":{
        "count":{
            "type":"integer"
        },
        "next":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "previous":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "results":{
            "items":{
                "$ref":"#/definitions/BulkHostDelete"
            },
            "type":"array"
        }
    },
    "required":[
        "count",
        "results"
    ],
    "type":"object"
}
```

Nested Schema : results

Type: `array`

[Show Source](#)

- [Array of:
  object](#200-definitions-BulkHostDelete-items-0)  [BulkHostDelete](#200-definitions-BulkHostDelete)

```
{
    "items":{
        "$ref":"#/definitions/BulkHostDelete"
    },
    "type":"array"
}
```

Nested Schema : BulkHostDelete

Type: `object`

[Show Source](#)

- [hosts(required):
  array](#200-definitions-BulkHostDelete-properties-hosts-properties-hosts-0)  [hosts](#200-definitions-BulkHostDelete-properties-hosts)

  Maximum Number of Items: `100000`

  List of hosts ids to be deleted, e.g. [105, 130, 131, 200]

```
{
    "properties":{
        "hosts":{
            "description":"List of hosts ids to be deleted, e.g. [105, 130, 131, 200]",
            "items":{
                "type":"string",
                "x-nullable":true
            },
            "maxItems":"100000",
            "type":"array"
        }
    },
    "required":[
        "hosts"
    ],
    "type":"object"
}
```

Nested Schema : hosts

Type: `array`

Maximum Number of Items: `100000`

List of hosts ids to be deleted, e.g. [105, 130, 131, 200]

[Show Source](#)

- [Array of:
  string](#200-definitions-BulkHostDelete-properties-hosts-items-items-0)

```
{
    "description":"List of hosts ids to be deleted, e.g. [105, 130, 131, 200]",
    "items":{
        "type":"string",
        "x-nullable":true
    },
    "maxItems":"100000",
    "type":"array"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-bulk-host_delete-post.html -->

This endpoint allows the client to delete multiple hosts from inventories.
They may do this by providing a list of hosts ID's to be deleted.

### Request

Supported Media Types

- application/json

Body ()

Root Schema : BulkHostDelete

Type: `object`

[Show Source](#)

- [hosts(required):
  array](#request-bodyparam-definitions-BulkHostDelete-properties-hosts-properties-hosts-0)  [hosts](#request-bodyparam-definitions-BulkHostDelete-properties-hosts)

  Maximum Number of Items: `100000`

  List of hosts ids to be deleted, e.g. [105, 130, 131, 200]

```
{
    "properties":{
        "hosts":{
            "description":"List of hosts ids to be deleted, e.g. [105, 130, 131, 200]",
            "items":{
                "type":"string",
                "x-nullable":true
            },
            "maxItems":"100000",
            "type":"array"
        }
    },
    "required":[
        "hosts"
    ],
    "type":"object"
}
```

Nested Schema : hosts

Type: `array`

Maximum Number of Items: `100000`

List of hosts ids to be deleted, e.g. [105, 130, 131, 200]

[Show Source](#)

- [Array of:
  string](#request-bodyparam-definitions-BulkHostDelete-properties-hosts-items-items-0)

```
{
    "description":"List of hosts ids to be deleted, e.g. [105, 130, 131, 200]",
    "items":{
        "type":"string",
        "x-nullable":true
    },
    "maxItems":"100000",
    "type":"array"
}
```

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

Body ()

Root Schema : BulkHostDelete

Type: `object`

[Show Source](#)

- [hosts(required):
  array](#201-definitions-BulkHostDelete-properties-hosts-properties-hosts-0)  [hosts](#201-definitions-BulkHostDelete-properties-hosts)

  Maximum Number of Items: `100000`

  List of hosts ids to be deleted, e.g. [105, 130, 131, 200]

```
{
    "properties":{
        "hosts":{
            "description":"List of hosts ids to be deleted, e.g. [105, 130, 131, 200]",
            "items":{
                "type":"string",
                "x-nullable":true
            },
            "maxItems":"100000",
            "type":"array"
        }
    },
    "required":[
        "hosts"
    ],
    "type":"object"
}
```

Nested Schema : hosts

Type: `array`

Maximum Number of Items: `100000`

List of hosts ids to be deleted, e.g. [105, 130, 131, 200]

[Show Source](#)

- [Array of:
  string](#201-definitions-BulkHostDelete-properties-hosts-items-items-0)

```
{
    "description":"List of hosts ids to be deleted, e.g. [105, 130, 131, 200]",
    "items":{
        "type":"string",
        "x-nullable":true
    },
    "maxItems":"100000",
    "type":"array"
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-bulk-job_launch-get.html -->

This endpoint allows the client to launch multiple UnifiedJobTemplates at a time, along side any launch time parameters that they would normally set at launch time.

### Request

Supported Media Types

- application/json

Query Parameters

- [page: integer](#request-query-param-0)

  A page number within the paginated result set.
- [page\_size: integer](#request-query-param-1)

  Number of results to return per page.
- [search: string](#request-query-param-2)

  A search term.

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 200 Response

Body ()

Root Schema : schema

Type: `object`

[Show Source](#)

- [count(required):
  integer](#200-paths--api-v2-bulk-job_launch--get-responses-200-schema-properties-count-properties-count-0)
- [next:
  string(uri)](#200-paths--api-v2-bulk-job_launch--get-responses-200-schema-properties-next-properties-next-0)
- [previous:
  string(uri)](#200-paths--api-v2-bulk-job_launch--get-responses-200-schema-properties-previous-properties-previous-0)
- [results(required):
  array](#200-paths--api-v2-bulk-job_launch--get-responses-200-schema-properties-results-properties-results-0)  [results](#200-paths--api-v2-bulk-job_launch--get-responses-200-schema-properties-results)

```
{
    "properties":{
        "count":{
            "type":"integer"
        },
        "next":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "previous":{
            "format":"uri",
            "type":"string",
            "x-nullable":true
        },
        "results":{
            "items":{
                "$ref":"#/definitions/BulkJobLaunch"
            },
            "type":"array"
        }
    },
    "required":[
        "count",
        "results"
    ],
    "type":"object"
}
```

Nested Schema : results

Type: `array`

[Show Source](#)

- [Array of:
  object](#200-definitions-BulkJobLaunch-items-0)  [BulkJobLaunch](#200-definitions-BulkJobLaunch)

```
{
    "items":{
        "$ref":"#/definitions/BulkJobLaunch"
    },
    "type":"array"
}
```

Nested Schema : BulkJobLaunch

Type: `object`

[Show Source](#)

- [description:
  string](#200-definitions-BulkJobLaunch-properties-description-properties-description-0)

  Title: `Description`

  Minimum Length: `1`
- [extra\_vars:
  object](#200-definitions-BulkJobLaunch-properties-extra_vars-properties-extra_vars-0)  [Extra vars](#200-definitions-BulkJobLaunch-properties-extra_vars)

  Title: `Extra vars`
- [inventory:
  integer](#200-definitions-BulkJobLaunch-properties-inventory-properties-inventory-0)

  Title: `Inventory`
- [job\_tags:
  string](#200-definitions-BulkJobLaunch-properties-job_tags-properties-job_tags-0)

  Title: `Job tags`

  Minimum Length: `1`
- [jobs(required):
  array](#200-definitions-BulkJobLaunch-properties-jobs-properties-jobs-0)  [jobs](#200-definitions-BulkJobLaunch-properties-jobs)

  List of jobs to be launched, JSON. e.g. [{"unified\_job\_template": 7}, {"unified\_job\_template": 10}]
- [limit:
  string](#200-definitions-BulkJobLaunch-properties-limit-properties-limit-0)

  Title: `Limit`

  Minimum Length: `1`
- [name:
  string](#200-definitions-BulkJobLaunch-properties-name-properties-name-0)

  Title: `Name`

  Maximum Length: `512`

  Default Value: `Bulk Job Launch`
- [organization:
  integer](#200-definitions-BulkJobLaunch-properties-organization-properties-organization-0)

  Title: `Organization`

  Inherit permissions from this organization. If not provided, a organization the user is a member of will be selected automatically.
- [scm\_branch:
  string](#200-definitions-BulkJobLaunch-properties-scm_branch-properties-scm_branch-0)

  Title: `Scm branch`

  Minimum Length: `1`
- [skip\_tags:
  string](#200-definitions-BulkJobLaunch-properties-skip_tags-properties-skip_tags-0)

  Title: `Skip tags`

  Minimum Length: `1`

```
{
    "properties":{
        "description":{
            "minLength":"1",
            "title":"Description",
            "type":"string"
        },
        "extra_vars":{
            "title":"Extra vars",
            "type":"object"
        },
        "inventory":{
            "title":"Inventory",
            "type":"integer"
        },
        "job_tags":{
            "minLength":"1",
            "title":"Job tags",
            "type":"string"
        },
        "jobs":{
            "description":"List of jobs to be launched, JSON. e.g. [{\"unified_job_template\": 7}, {\"unified_job_template\": 10}]",
            "items":{
                "$ref":"#/definitions/BulkJobNode"
            },
            "type":"array"
        },
        "limit":{
            "minLength":"1",
            "title":"Limit",
            "type":"string"
        },
        "name":{
            "default":"Bulk Job Launch",
            "maxLength":"512",
            "title":"Name",
            "type":"string"
        },
        "organization":{
            "description":"Inherit permissions from this organization. If not provided, a organization the user is a member of will be selected automatically.",
            "title":"Organization",
            "type":"integer",
            "x-nullable":true
        },
        "scm_branch":{
            "minLength":"1",
            "title":"Scm branch",
            "type":"string"
        },
        "skip_tags":{
            "minLength":"1",
            "title":"Skip tags",
            "type":"string"
        }
    },
    "required":[
        "jobs"
    ],
    "type":"object"
}
```

Nested Schema : Extra vars

Type: `object`

Title: `Extra vars`

Nested Schema : jobs

Type: `array`

List of jobs to be launched, JSON. e.g. [{"unified\_job\_template": 7}, {"unified\_job\_template": 10}]

[Show Source](#)

- [Array of:
  object](#200-definitions-BulkJobNode-items-0)  [BulkJobNode](#200-definitions-BulkJobNode)

  List of jobs to be launched, JSON. e.g. [{"unified\_job\_template": 7}, {"unified\_job\_template": 10}]

```
{
    "description":"List of jobs to be launched, JSON. e.g. [{\"unified_job_template\": 7}, {\"unified_job_template\": 10}]",
    "items":{
        "$ref":"#/definitions/BulkJobNode"
    },
    "type":"array"
}
```

Nested Schema : BulkJobNode

Type: `object`

List of jobs to be launched, JSON. e.g. [{"unified\_job\_template": 7}, {"unified\_job\_template": 10}]

[Show Source](#)

- [all\_parents\_must\_converge:
  boolean](#200-definitions-BulkJobNode-properties-all_parents_must_converge-properties-all_parents_must_converge-0)

  Title: `All parents must converge`

  If enabled then the node will only run if all of the parent nodes have met the criteria to reach this node
- [always\_nodes:
  array](#200-definitions-BulkJobNode-properties-always_nodes-properties-always_nodes-0)  [always\_nodes](#200-definitions-BulkJobNode-properties-always_nodes)

  Read Only: `true`

  Unique Items Required: `true`
- [created:
  string](#200-definitions-BulkJobNode-properties-created-properties-created-0)

  Title: `Created`

  Read Only: `true`
- [credentials:
  array](#200-definitions-BulkJobNode-properties-credentials-properties-credentials-0)  [credentials](#200-definitions-BulkJobNode-properties-credentials)
- [diff\_mode:
  boolean](#200-definitions-BulkJobNode-properties-diff_mode-properties-diff_mode-0)

  Title: `Diff mode`
- [do\_not\_run:
  boolean](#200-definitions-BulkJobNode-properties-do_not_run-properties-do_not_run-0)

  Title: `Do not run`

  Indicates that a job will not be created when True. Workflow runtime semantics will mark this True if the node is in a path that will decidedly not be ran. A value of False means the node may not run.
- [execution\_environment:
  integer](#200-definitions-BulkJobNode-properties-execution_environment-properties-execution_environment-0)

  Title: `Execution environment`

  Minimum Value: `1`
- [extra\_data:
  object](#200-definitions-BulkJobNode-properties-extra_data-properties-extra_data-0)  [Extra data](#200-definitions-BulkJobNode-properties-extra_data)

  Title: `Extra data`
- [failure\_nodes:
  array](#200-definitions-BulkJobNode-properties-failure_nodes-properties-failure_nodes-0)  [failure\_nodes](#200-definitions-BulkJobNode-properties-failure_nodes)

  Read Only: `true`

  Unique Items Required: `true`
- [forks:
  integer](#200-definitions-BulkJobNode-properties-forks-properties-forks-0)

  Title: `Forks`

  Minimum Value: `0`
- [id:
  integer](#200-definitions-BulkJobNode-properties-id-properties-id-0)

  Title: `ID`

  Read Only: `true`
- [identifier:
  string](#200-definitions-BulkJobNode-properties-identifier-properties-identifier-0)

  Title: `Identifier`

  Maximum Length: `512`

  An identifier coresponding to the workflow job template node that this node was created from.
- [instance\_groups:
  array](#200-definitions-BulkJobNode-properties-instance_groups-properties-instance_groups-0)  [instance\_groups](#200-definitions-BulkJobNode-properties-instance_groups)
- [inventory:
  integer](#200-definitions-BulkJobNode-properties-inventory-properties-inventory-0)

  Title: `Inventory`

  Minimum Value: `1`
- [job:
  integer](#200-definitions-BulkJobNode-properties-job-properties-job-0)

  Title: `Job`
- [job\_slice\_count:
  integer](#200-definitions-BulkJobNode-properties-job_slice_count-properties-job_slice_count-0)

  Title: `Job slice count`

  Minimum Value: `0`
- [job\_tags:
  string](#200-definitions-BulkJobNode-properties-job_tags-properties-job_tags-0)

  Title: `Job tags`
- [job\_type:
  string](#200-definitions-BulkJobNode-properties-job_type-properties-job_type-0)

  Title: `Job type`

  Allowed Values: `[
  "run",
  "check"
  ]`
- [labels:
  array](#200-definitions-BulkJobNode-properties-labels-properties-labels-0)  [labels](#200-definitions-BulkJobNode-properties-labels)
- [limit:
  string](#200-definitions-BulkJobNode-properties-limit-properties-limit-0)

  Title: `Limit`
- [modified:
  string](#200-definitions-BulkJobNode-properties-modified-properties-modified-0)

  Title: `Modified`

  Read Only: `true`
- [related:
  string](#200-definitions-BulkJobNode-properties-related-properties-related-0)

  Title: `Related`

  Read Only: `true`
- [scm\_branch:
  string](#200-definitions-BulkJobNode-properties-scm_branch-properties-scm_branch-0)

  Title: `Scm branch`
- [skip\_tags:
  string](#200-definitions-BulkJobNode-properties-skip_tags-properties-skip_tags-0)

  Title: `Skip tags`
- [success\_nodes:
  array](#200-definitions-BulkJobNode-properties-success_nodes-properties-success_nodes-0)  [success\_nodes](#200-definitions-BulkJobNode-properties-success_nodes)

  Read Only: `true`

  Unique Items Required: `true`
- [summary\_fields:
  string](#200-definitions-BulkJobNode-properties-summary_fields-properties-summary_fields-0)

  Title: `Summary fields`

  Read Only: `true`
- [timeout:
  integer](#200-definitions-BulkJobNode-properties-timeout-properties-timeout-0)

  Title: `Timeout`
- [type:
  string](#200-definitions-BulkJobNode-properties-type-properties-type-0)

  Title: `Type`

  Read Only: `true`
- [unified\_job\_template(required):
  integer](#200-definitions-BulkJobNode-properties-unified_job_template-properties-unified_job_template-0)

  Title: `Unified job template`

  Minimum Value: `1`

  Primary key of the template for this job, can be a job template or inventory source.
- [url:
  string](#200-definitions-BulkJobNode-properties-url-properties-url-0)

  Title: `Url`

  Read Only: `true`
- [verbosity:
  string](#200-definitions-BulkJobNode-properties-verbosity-properties-verbosity-0)

  Title: `Verbosity`

  Allowed Values: `[
  "0",
  "1",
  "2",
  "3",
  "4",
  "5"
  ]`
- [workflow\_job:
  string](#200-definitions-BulkJobNode-properties-workflow_job-properties-workflow_job-0)

  Title: `Workflow job`

```
{
    "description":"List of jobs to be launched, JSON. e.g. [{\"unified_job_template\": 7}, {\"unified_job_template\": 10}]",
    "properties":{
        "all_parents_must_converge":{
            "description":"If enabled then the node will only run if all of the parent nodes have met the criteria to reach this node",
            "title":"All parents must converge",
            "type":"boolean",
            "x-nullable":true
        },
        "always_nodes":{
            "items":{
                "type":"integer"
            },
            "readOnly":true,
            "type":"array",
            "uniqueItems":true
        },
        "created":{
            "readOnly":true,
            "title":"Created",
            "type":"string"
        },
        "credentials":{
            "items":{
                "minimum":"1",
                "type":"integer"
            },
            "type":"array"
        },
        "diff_mode":{
            "title":"Diff mode",
            "type":"boolean",
            "x-nullable":true
        },
        "do_not_run":{
            "description":"Indicates that a job will not be created when True. Workflow runtime semantics will mark this True if the node is in a path that will decidedly not be ran. A value of False means the node may not run.",
            "title":"Do not run",
            "type":"boolean",
            "x-nullable":true
        },
        "execution_environment":{
            "minimum":"1",
            "title":"Execution environment",
            "type":"integer"
        },
        "extra_data":{
            "title":"Extra data",
            "type":"object"
        },
        "failure_nodes":{
            "items":{
                "type":"integer"
            },
            "readOnly":true,
            "type":"array",
            "uniqueItems":true
        },
        "forks":{
            "minimum":"0",
            "title":"Forks",
            "type":"integer",
            "x-nullable":true
        },
        "id":{
            "readOnly":true,
            "title":"ID",
            "type":"integer"
        },
        "identifier":{
            "description":"An identifier coresponding to the workflow job template node that this node was created from.",
            "maxLength":"512",
            "title":"Identifier",
            "type":"string",
            "x-nullable":true
        },
        "instance_groups":{
            "items":{
                "minimum":"1",
                "type":"integer"
            },
            "type":"array"
        },
        "inventory":{
            "minimum":"1",
            "title":"Inventory",
            "type":"integer"
        },
        "job":{
            "title":"Job",
            "type":"integer",
            "x-nullable":true
        },
        "job_slice_count":{
            "minimum":"0",
            "title":"Job slice count",
            "type":"integer",
            "x-nullable":true
        },
        "job_tags":{
            "title":"Job tags",
            "type":"string",
            "x-nullable":true
        },
        "job_type":{
            "enum":[
                "run",
                "check"
            ],
            "title":"Job type",
            "type":"string",
            "x-nullable":true
        },
        "labels":{
            "items":{
                "minimum":"1",
                "type":"integer"
            },
            "type":"array"
        },
        "limit":{
            "title":"Limit",
            "type":"string",
            "x-nullable":true
        },
        "modified":{
            "readOnly":true,
            "title":"Modified",
            "type":"string"
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "scm_branch":{
            "title":"Scm branch",
            "type":"string",
            "x-nullable":true
        },
        "skip_tags":{
            "title":"Skip tags",
            "type":"string",
            "x-nullable":true
        },
        "success_nodes":{
            "items":{
                "type":"integer"
            },
            "readOnly":true,
            "type":"array",
            "uniqueItems":true
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "timeout":{
            "title":"Timeout",
            "type":"integer",
            "x-nullable":true
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "unified_job_template":{
            "description":"Primary key of the template for this job, can be a job template or inventory source.",
            "minimum":"1",
            "title":"Unified job template",
            "type":"integer"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        },
        "verbosity":{
            "enum":[
                "0",
                "1",
                "2",
                "3",
                "4",
                "5"
            ],
            "title":"Verbosity",
            "type":"string",
            "x-nullable":true
        },
        "workflow_job":{
            "title":"Workflow job",
            "type":"string",
            "x-nullable":true
        }
    },
    "required":[
        "unified_job_template"
    ],
    "type":"object"
}
```

Nested Schema : always\_nodes

Type: `array`

Read Only: `true`

Unique Items Required: `true`

[Show Source](#)

- [Array of:
  integer](#200-definitions-BulkJobNode-properties-always_nodes-items-items-0)

```
{
    "items":{
        "type":"integer"
    },
    "readOnly":true,
    "type":"array",
    "uniqueItems":true
}
```

Nested Schema : credentials

Type: `array`

[Show Source](#)

- [Array of:
  integer](#200-definitions-BulkJobNode-properties-credentials-items-items-0)

  Minimum Value: `1`

```
{
    "items":{
        "minimum":"1",
        "type":"integer"
    },
    "type":"array"
}
```

Nested Schema : Extra data

Type: `object`

Title: `Extra data`

Nested Schema : failure\_nodes

Type: `array`

Read Only: `true`

Unique Items Required: `true`

[Show Source](#)

- [Array of:
  integer](#200-definitions-BulkJobNode-properties-failure_nodes-items-items-0)

```
{
    "items":{
        "type":"integer"
    },
    "readOnly":true,
    "type":"array",
    "uniqueItems":true
}
```

Nested Schema : instance\_groups

Type: `array`

[Show Source](#)

- [Array of:
  integer](#200-definitions-BulkJobNode-properties-instance_groups-items-items-0)

  Minimum Value: `1`

```
{
    "items":{
        "minimum":"1",
        "type":"integer"
    },
    "type":"array"
}
```

Nested Schema : labels

Type: `array`

[Show Source](#)

- [Array of:
  integer](#200-definitions-BulkJobNode-properties-labels-items-items-0)

  Minimum Value: `1`

```
{
    "items":{
        "minimum":"1",
        "type":"integer"
    },
    "type":"array"
}
```

Nested Schema : success\_nodes

Type: `array`

Read Only: `true`

Unique Items Required: `true`

[Show Source](#)

- [Array of:
  integer](#200-definitions-BulkJobNode-properties-success_nodes-items-items-0)

```
{
    "items":{
        "type":"integer"
    },
    "readOnly":true,
    "type":"array",
    "uniqueItems":true
}
```

[Back to Top](#top)


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux-automation-manager/2/olam-api-cli2.3/op-api-v2-bulk-job_launch-post.html -->

This endpoint allows the client to launch multiple UnifiedJobTemplates at a time, along side any launch time parameters that they would normally set at launch time.

### Request

Supported Media Types

- application/json

Body ()

Root Schema : BulkJobLaunch

Type: `object`

[Show Source](#)

- [description:
  string](#request-bodyparam-definitions-BulkJobLaunch-properties-description-properties-description-0)

  Title: `Description`

  Minimum Length: `1`
- [extra\_vars:
  object](#request-bodyparam-definitions-BulkJobLaunch-properties-extra_vars-properties-extra_vars-0)  [Extra vars](#request-bodyparam-definitions-BulkJobLaunch-properties-extra_vars)

  Title: `Extra vars`
- [inventory:
  integer](#request-bodyparam-definitions-BulkJobLaunch-properties-inventory-properties-inventory-0)

  Title: `Inventory`
- [job\_tags:
  string](#request-bodyparam-definitions-BulkJobLaunch-properties-job_tags-properties-job_tags-0)

  Title: `Job tags`

  Minimum Length: `1`
- [jobs(required):
  array](#request-bodyparam-definitions-BulkJobLaunch-properties-jobs-properties-jobs-0)  [jobs](#request-bodyparam-definitions-BulkJobLaunch-properties-jobs)

  List of jobs to be launched, JSON. e.g. [{"unified\_job\_template": 7}, {"unified\_job\_template": 10}]
- [limit:
  string](#request-bodyparam-definitions-BulkJobLaunch-properties-limit-properties-limit-0)

  Title: `Limit`

  Minimum Length: `1`
- [name:
  string](#request-bodyparam-definitions-BulkJobLaunch-properties-name-properties-name-0)

  Title: `Name`

  Maximum Length: `512`

  Default Value: `Bulk Job Launch`
- [organization:
  integer](#request-bodyparam-definitions-BulkJobLaunch-properties-organization-properties-organization-0)

  Title: `Organization`

  Inherit permissions from this organization. If not provided, a organization the user is a member of will be selected automatically.
- [scm\_branch:
  string](#request-bodyparam-definitions-BulkJobLaunch-properties-scm_branch-properties-scm_branch-0)

  Title: `Scm branch`

  Minimum Length: `1`
- [skip\_tags:
  string](#request-bodyparam-definitions-BulkJobLaunch-properties-skip_tags-properties-skip_tags-0)

  Title: `Skip tags`

  Minimum Length: `1`

```
{
    "properties":{
        "description":{
            "minLength":"1",
            "title":"Description",
            "type":"string"
        },
        "extra_vars":{
            "title":"Extra vars",
            "type":"object"
        },
        "inventory":{
            "title":"Inventory",
            "type":"integer"
        },
        "job_tags":{
            "minLength":"1",
            "title":"Job tags",
            "type":"string"
        },
        "jobs":{
            "description":"List of jobs to be launched, JSON. e.g. [{\"unified_job_template\": 7}, {\"unified_job_template\": 10}]",
            "items":{
                "$ref":"#/definitions/BulkJobNode"
            },
            "type":"array"
        },
        "limit":{
            "minLength":"1",
            "title":"Limit",
            "type":"string"
        },
        "name":{
            "default":"Bulk Job Launch",
            "maxLength":"512",
            "title":"Name",
            "type":"string"
        },
        "organization":{
            "description":"Inherit permissions from this organization. If not provided, a organization the user is a member of will be selected automatically.",
            "title":"Organization",
            "type":"integer",
            "x-nullable":true
        },
        "scm_branch":{
            "minLength":"1",
            "title":"Scm branch",
            "type":"string"
        },
        "skip_tags":{
            "minLength":"1",
            "title":"Skip tags",
            "type":"string"
        }
    },
    "required":[
        "jobs"
    ],
    "type":"object"
}
```

Nested Schema : Extra vars

Type: `object`

Title: `Extra vars`

Nested Schema : jobs

Type: `array`

List of jobs to be launched, JSON. e.g. [{"unified\_job\_template": 7}, {"unified\_job\_template": 10}]

[Show Source](#)

- [Array of:
  object](#request-bodyparam-definitions-BulkJobNode-items-0)  [BulkJobNode](#request-bodyparam-definitions-BulkJobNode)

  List of jobs to be launched, JSON. e.g. [{"unified\_job\_template": 7}, {"unified\_job\_template": 10}]

```
{
    "description":"List of jobs to be launched, JSON. e.g. [{\"unified_job_template\": 7}, {\"unified_job_template\": 10}]",
    "items":{
        "$ref":"#/definitions/BulkJobNode"
    },
    "type":"array"
}
```

Nested Schema : BulkJobNode

Type: `object`

List of jobs to be launched, JSON. e.g. [{"unified\_job\_template": 7}, {"unified\_job\_template": 10}]

[Show Source](#)

- [all\_parents\_must\_converge:
  boolean](#request-bodyparam-definitions-BulkJobNode-properties-all_parents_must_converge-properties-all_parents_must_converge-0)

  Title: `All parents must converge`

  If enabled then the node will only run if all of the parent nodes have met the criteria to reach this node
- [always\_nodes:
  array](#request-bodyparam-definitions-BulkJobNode-properties-always_nodes-properties-always_nodes-0)  [always\_nodes](#request-bodyparam-definitions-BulkJobNode-properties-always_nodes)

  Read Only: `true`

  Unique Items Required: `true`
- [created:
  string](#request-bodyparam-definitions-BulkJobNode-properties-created-properties-created-0)

  Title: `Created`

  Read Only: `true`
- [credentials:
  array](#request-bodyparam-definitions-BulkJobNode-properties-credentials-properties-credentials-0)  [credentials](#request-bodyparam-definitions-BulkJobNode-properties-credentials)
- [diff\_mode:
  boolean](#request-bodyparam-definitions-BulkJobNode-properties-diff_mode-properties-diff_mode-0)

  Title: `Diff mode`
- [do\_not\_run:
  boolean](#request-bodyparam-definitions-BulkJobNode-properties-do_not_run-properties-do_not_run-0)

  Title: `Do not run`

  Indicates that a job will not be created when True. Workflow runtime semantics will mark this True if the node is in a path that will decidedly not be ran. A value of False means the node may not run.
- [execution\_environment:
  integer](#request-bodyparam-definitions-BulkJobNode-properties-execution_environment-properties-execution_environment-0)

  Title: `Execution environment`

  Minimum Value: `1`
- [extra\_data:
  object](#request-bodyparam-definitions-BulkJobNode-properties-extra_data-properties-extra_data-0)  [Extra data](#request-bodyparam-definitions-BulkJobNode-properties-extra_data)

  Title: `Extra data`
- [failure\_nodes:
  array](#request-bodyparam-definitions-BulkJobNode-properties-failure_nodes-properties-failure_nodes-0)  [failure\_nodes](#request-bodyparam-definitions-BulkJobNode-properties-failure_nodes)

  Read Only: `true`

  Unique Items Required: `true`
- [forks:
  integer](#request-bodyparam-definitions-BulkJobNode-properties-forks-properties-forks-0)

  Title: `Forks`

  Minimum Value: `0`
- [id:
  integer](#request-bodyparam-definitions-BulkJobNode-properties-id-properties-id-0)

  Title: `ID`

  Read Only: `true`
- [identifier:
  string](#request-bodyparam-definitions-BulkJobNode-properties-identifier-properties-identifier-0)

  Title: `Identifier`

  Maximum Length: `512`

  An identifier coresponding to the workflow job template node that this node was created from.
- [instance\_groups:
  array](#request-bodyparam-definitions-BulkJobNode-properties-instance_groups-properties-instance_groups-0)  [instance\_groups](#request-bodyparam-definitions-BulkJobNode-properties-instance_groups)
- [inventory:
  integer](#request-bodyparam-definitions-BulkJobNode-properties-inventory-properties-inventory-0)

  Title: `Inventory`

  Minimum Value: `1`
- [job:
  integer](#request-bodyparam-definitions-BulkJobNode-properties-job-properties-job-0)

  Title: `Job`
- [job\_slice\_count:
  integer](#request-bodyparam-definitions-BulkJobNode-properties-job_slice_count-properties-job_slice_count-0)

  Title: `Job slice count`

  Minimum Value: `0`
- [job\_tags:
  string](#request-bodyparam-definitions-BulkJobNode-properties-job_tags-properties-job_tags-0)

  Title: `Job tags`
- [job\_type:
  string](#request-bodyparam-definitions-BulkJobNode-properties-job_type-properties-job_type-0)

  Title: `Job type`

  Allowed Values: `[
  "run",
  "check"
  ]`
- [labels:
  array](#request-bodyparam-definitions-BulkJobNode-properties-labels-properties-labels-0)  [labels](#request-bodyparam-definitions-BulkJobNode-properties-labels)
- [limit:
  string](#request-bodyparam-definitions-BulkJobNode-properties-limit-properties-limit-0)

  Title: `Limit`
- [modified:
  string](#request-bodyparam-definitions-BulkJobNode-properties-modified-properties-modified-0)

  Title: `Modified`

  Read Only: `true`
- [related:
  string](#request-bodyparam-definitions-BulkJobNode-properties-related-properties-related-0)

  Title: `Related`

  Read Only: `true`
- [scm\_branch:
  string](#request-bodyparam-definitions-BulkJobNode-properties-scm_branch-properties-scm_branch-0)

  Title: `Scm branch`
- [skip\_tags:
  string](#request-bodyparam-definitions-BulkJobNode-properties-skip_tags-properties-skip_tags-0)

  Title: `Skip tags`
- [success\_nodes:
  array](#request-bodyparam-definitions-BulkJobNode-properties-success_nodes-properties-success_nodes-0)  [success\_nodes](#request-bodyparam-definitions-BulkJobNode-properties-success_nodes)

  Read Only: `true`

  Unique Items Required: `true`
- [summary\_fields:
  string](#request-bodyparam-definitions-BulkJobNode-properties-summary_fields-properties-summary_fields-0)

  Title: `Summary fields`

  Read Only: `true`
- [timeout:
  integer](#request-bodyparam-definitions-BulkJobNode-properties-timeout-properties-timeout-0)

  Title: `Timeout`
- [type:
  string](#request-bodyparam-definitions-BulkJobNode-properties-type-properties-type-0)

  Title: `Type`

  Read Only: `true`
- [unified\_job\_template(required):
  integer](#request-bodyparam-definitions-BulkJobNode-properties-unified_job_template-properties-unified_job_template-0)

  Title: `Unified job template`

  Minimum Value: `1`

  Primary key of the template for this job, can be a job template or inventory source.
- [url:
  string](#request-bodyparam-definitions-BulkJobNode-properties-url-properties-url-0)

  Title: `Url`

  Read Only: `true`
- [verbosity:
  string](#request-bodyparam-definitions-BulkJobNode-properties-verbosity-properties-verbosity-0)

  Title: `Verbosity`

  Allowed Values: `[
  "0",
  "1",
  "2",
  "3",
  "4",
  "5"
  ]`
- [workflow\_job:
  string](#request-bodyparam-definitions-BulkJobNode-properties-workflow_job-properties-workflow_job-0)

  Title: `Workflow job`

```
{
    "description":"List of jobs to be launched, JSON. e.g. [{\"unified_job_template\": 7}, {\"unified_job_template\": 10}]",
    "properties":{
        "all_parents_must_converge":{
            "description":"If enabled then the node will only run if all of the parent nodes have met the criteria to reach this node",
            "title":"All parents must converge",
            "type":"boolean",
            "x-nullable":true
        },
        "always_nodes":{
            "items":{
                "type":"integer"
            },
            "readOnly":true,
            "type":"array",
            "uniqueItems":true
        },
        "created":{
            "readOnly":true,
            "title":"Created",
            "type":"string"
        },
        "credentials":{
            "items":{
                "minimum":"1",
                "type":"integer"
            },
            "type":"array"
        },
        "diff_mode":{
            "title":"Diff mode",
            "type":"boolean",
            "x-nullable":true
        },
        "do_not_run":{
            "description":"Indicates that a job will not be created when True. Workflow runtime semantics will mark this True if the node is in a path that will decidedly not be ran. A value of False means the node may not run.",
            "title":"Do not run",
            "type":"boolean",
            "x-nullable":true
        },
        "execution_environment":{
            "minimum":"1",
            "title":"Execution environment",
            "type":"integer"
        },
        "extra_data":{
            "title":"Extra data",
            "type":"object"
        },
        "failure_nodes":{
            "items":{
                "type":"integer"
            },
            "readOnly":true,
            "type":"array",
            "uniqueItems":true
        },
        "forks":{
            "minimum":"0",
            "title":"Forks",
            "type":"integer",
            "x-nullable":true
        },
        "id":{
            "readOnly":true,
            "title":"ID",
            "type":"integer"
        },
        "identifier":{
            "description":"An identifier coresponding to the workflow job template node that this node was created from.",
            "maxLength":"512",
            "title":"Identifier",
            "type":"string",
            "x-nullable":true
        },
        "instance_groups":{
            "items":{
                "minimum":"1",
                "type":"integer"
            },
            "type":"array"
        },
        "inventory":{
            "minimum":"1",
            "title":"Inventory",
            "type":"integer"
        },
        "job":{
            "title":"Job",
            "type":"integer",
            "x-nullable":true
        },
        "job_slice_count":{
            "minimum":"0",
            "title":"Job slice count",
            "type":"integer",
            "x-nullable":true
        },
        "job_tags":{
            "title":"Job tags",
            "type":"string",
            "x-nullable":true
        },
        "job_type":{
            "enum":[
                "run",
                "check"
            ],
            "title":"Job type",
            "type":"string",
            "x-nullable":true
        },
        "labels":{
            "items":{
                "minimum":"1",
                "type":"integer"
            },
            "type":"array"
        },
        "limit":{
            "title":"Limit",
            "type":"string",
            "x-nullable":true
        },
        "modified":{
            "readOnly":true,
            "title":"Modified",
            "type":"string"
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "scm_branch":{
            "title":"Scm branch",
            "type":"string",
            "x-nullable":true
        },
        "skip_tags":{
            "title":"Skip tags",
            "type":"string",
            "x-nullable":true
        },
        "success_nodes":{
            "items":{
                "type":"integer"
            },
            "readOnly":true,
            "type":"array",
            "uniqueItems":true
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "timeout":{
            "title":"Timeout",
            "type":"integer",
            "x-nullable":true
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "unified_job_template":{
            "description":"Primary key of the template for this job, can be a job template or inventory source.",
            "minimum":"1",
            "title":"Unified job template",
            "type":"integer"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        },
        "verbosity":{
            "enum":[
                "0",
                "1",
                "2",
                "3",
                "4",
                "5"
            ],
            "title":"Verbosity",
            "type":"string",
            "x-nullable":true
        },
        "workflow_job":{
            "title":"Workflow job",
            "type":"string",
            "x-nullable":true
        }
    },
    "required":[
        "unified_job_template"
    ],
    "type":"object"
}
```

Nested Schema : always\_nodes

Type: `array`

Read Only: `true`

Unique Items Required: `true`

[Show Source](#)

- [Array of:
  integer](#request-bodyparam-definitions-BulkJobNode-properties-always_nodes-items-items-0)

```
{
    "items":{
        "type":"integer"
    },
    "readOnly":true,
    "type":"array",
    "uniqueItems":true
}
```

Nested Schema : credentials

Type: `array`

[Show Source](#)

- [Array of:
  integer](#request-bodyparam-definitions-BulkJobNode-properties-credentials-items-items-0)

  Minimum Value: `1`

```
{
    "items":{
        "minimum":"1",
        "type":"integer"
    },
    "type":"array"
}
```

Nested Schema : Extra data

Type: `object`

Title: `Extra data`

Nested Schema : failure\_nodes

Type: `array`

Read Only: `true`

Unique Items Required: `true`

[Show Source](#)

- [Array of:
  integer](#request-bodyparam-definitions-BulkJobNode-properties-failure_nodes-items-items-0)

```
{
    "items":{
        "type":"integer"
    },
    "readOnly":true,
    "type":"array",
    "uniqueItems":true
}
```

Nested Schema : instance\_groups

Type: `array`

[Show Source](#)

- [Array of:
  integer](#request-bodyparam-definitions-BulkJobNode-properties-instance_groups-items-items-0)

  Minimum Value: `1`

```
{
    "items":{
        "minimum":"1",
        "type":"integer"
    },
    "type":"array"
}
```

Nested Schema : labels

Type: `array`

[Show Source](#)

- [Array of:
  integer](#request-bodyparam-definitions-BulkJobNode-properties-labels-items-items-0)

  Minimum Value: `1`

```
{
    "items":{
        "minimum":"1",
        "type":"integer"
    },
    "type":"array"
}
```

Nested Schema : success\_nodes

Type: `array`

Read Only: `true`

Unique Items Required: `true`

[Show Source](#)

- [Array of:
  integer](#request-bodyparam-definitions-BulkJobNode-properties-success_nodes-items-items-0)

```
{
    "items":{
        "type":"integer"
    },
    "readOnly":true,
    "type":"array",
    "uniqueItems":true
}
```

[Back to Top](#top)

### Response

Supported Media Types

- application/json

#### 201 Response

Body ()

Root Schema : BulkJobLaunch

Type: `object`

[Show Source](#)

- [description:
  string](#201-definitions-BulkJobLaunch-properties-description-properties-description-0)

  Title: `Description`

  Minimum Length: `1`
- [extra\_vars:
  object](#201-definitions-BulkJobLaunch-properties-extra_vars-properties-extra_vars-0)  [Extra vars](#201-definitions-BulkJobLaunch-properties-extra_vars)

  Title: `Extra vars`
- [inventory:
  integer](#201-definitions-BulkJobLaunch-properties-inventory-properties-inventory-0)

  Title: `Inventory`
- [job\_tags:
  string](#201-definitions-BulkJobLaunch-properties-job_tags-properties-job_tags-0)

  Title: `Job tags`

  Minimum Length: `1`
- [jobs(required):
  array](#201-definitions-BulkJobLaunch-properties-jobs-properties-jobs-0)  [jobs](#201-definitions-BulkJobLaunch-properties-jobs)

  List of jobs to be launched, JSON. e.g. [{"unified\_job\_template": 7}, {"unified\_job\_template": 10}]
- [limit:
  string](#201-definitions-BulkJobLaunch-properties-limit-properties-limit-0)

  Title: `Limit`

  Minimum Length: `1`
- [name:
  string](#201-definitions-BulkJobLaunch-properties-name-properties-name-0)

  Title: `Name`

  Maximum Length: `512`

  Default Value: `Bulk Job Launch`
- [organization:
  integer](#201-definitions-BulkJobLaunch-properties-organization-properties-organization-0)

  Title: `Organization`

  Inherit permissions from this organization. If not provided, a organization the user is a member of will be selected automatically.
- [scm\_branch:
  string](#201-definitions-BulkJobLaunch-properties-scm_branch-properties-scm_branch-0)

  Title: `Scm branch`

  Minimum Length: `1`
- [skip\_tags:
  string](#201-definitions-BulkJobLaunch-properties-skip_tags-properties-skip_tags-0)

  Title: `Skip tags`

  Minimum Length: `1`

```
{
    "properties":{
        "description":{
            "minLength":"1",
            "title":"Description",
            "type":"string"
        },
        "extra_vars":{
            "title":"Extra vars",
            "type":"object"
        },
        "inventory":{
            "title":"Inventory",
            "type":"integer"
        },
        "job_tags":{
            "minLength":"1",
            "title":"Job tags",
            "type":"string"
        },
        "jobs":{
            "description":"List of jobs to be launched, JSON. e.g. [{\"unified_job_template\": 7}, {\"unified_job_template\": 10}]",
            "items":{
                "$ref":"#/definitions/BulkJobNode"
            },
            "type":"array"
        },
        "limit":{
            "minLength":"1",
            "title":"Limit",
            "type":"string"
        },
        "name":{
            "default":"Bulk Job Launch",
            "maxLength":"512",
            "title":"Name",
            "type":"string"
        },
        "organization":{
            "description":"Inherit permissions from this organization. If not provided, a organization the user is a member of will be selected automatically.",
            "title":"Organization",
            "type":"integer",
            "x-nullable":true
        },
        "scm_branch":{
            "minLength":"1",
            "title":"Scm branch",
            "type":"string"
        },
        "skip_tags":{
            "minLength":"1",
            "title":"Skip tags",
            "type":"string"
        }
    },
    "required":[
        "jobs"
    ],
    "type":"object"
}
```

Nested Schema : Extra vars

Type: `object`

Title: `Extra vars`

Nested Schema : jobs

Type: `array`

List of jobs to be launched, JSON. e.g. [{"unified\_job\_template": 7}, {"unified\_job\_template": 10}]

[Show Source](#)

- [Array of:
  object](#201-definitions-BulkJobNode-items-0)  [BulkJobNode](#201-definitions-BulkJobNode)

  List of jobs to be launched, JSON. e.g. [{"unified\_job\_template": 7}, {"unified\_job\_template": 10}]

```
{
    "description":"List of jobs to be launched, JSON. e.g. [{\"unified_job_template\": 7}, {\"unified_job_template\": 10}]",
    "items":{
        "$ref":"#/definitions/BulkJobNode"
    },
    "type":"array"
}
```

Nested Schema : BulkJobNode

Type: `object`

List of jobs to be launched, JSON. e.g. [{"unified\_job\_template": 7}, {"unified\_job\_template": 10}]

[Show Source](#)

- [all\_parents\_must\_converge:
  boolean](#201-definitions-BulkJobNode-properties-all_parents_must_converge-properties-all_parents_must_converge-0)

  Title: `All parents must converge`

  If enabled then the node will only run if all of the parent nodes have met the criteria to reach this node
- [always\_nodes:
  array](#201-definitions-BulkJobNode-properties-always_nodes-properties-always_nodes-0)  [always\_nodes](#201-definitions-BulkJobNode-properties-always_nodes)

  Read Only: `true`

  Unique Items Required: `true`
- [created:
  string](#201-definitions-BulkJobNode-properties-created-properties-created-0)

  Title: `Created`

  Read Only: `true`
- [credentials:
  array](#201-definitions-BulkJobNode-properties-credentials-properties-credentials-0)  [credentials](#201-definitions-BulkJobNode-properties-credentials)
- [diff\_mode:
  boolean](#201-definitions-BulkJobNode-properties-diff_mode-properties-diff_mode-0)

  Title: `Diff mode`
- [do\_not\_run:
  boolean](#201-definitions-BulkJobNode-properties-do_not_run-properties-do_not_run-0)

  Title: `Do not run`

  Indicates that a job will not be created when True. Workflow runtime semantics will mark this True if the node is in a path that will decidedly not be ran. A value of False means the node may not run.
- [execution\_environment:
  integer](#201-definitions-BulkJobNode-properties-execution_environment-properties-execution_environment-0)

  Title: `Execution environment`

  Minimum Value: `1`
- [extra\_data:
  object](#201-definitions-BulkJobNode-properties-extra_data-properties-extra_data-0)  [Extra data](#201-definitions-BulkJobNode-properties-extra_data)

  Title: `Extra data`
- [failure\_nodes:
  array](#201-definitions-BulkJobNode-properties-failure_nodes-properties-failure_nodes-0)  [failure\_nodes](#201-definitions-BulkJobNode-properties-failure_nodes)

  Read Only: `true`

  Unique Items Required: `true`
- [forks:
  integer](#201-definitions-BulkJobNode-properties-forks-properties-forks-0)

  Title: `Forks`

  Minimum Value: `0`
- [id:
  integer](#201-definitions-BulkJobNode-properties-id-properties-id-0)

  Title: `ID`

  Read Only: `true`
- [identifier:
  string](#201-definitions-BulkJobNode-properties-identifier-properties-identifier-0)

  Title: `Identifier`

  Maximum Length: `512`

  An identifier coresponding to the workflow job template node that this node was created from.
- [instance\_groups:
  array](#201-definitions-BulkJobNode-properties-instance_groups-properties-instance_groups-0)  [instance\_groups](#201-definitions-BulkJobNode-properties-instance_groups)
- [inventory:
  integer](#201-definitions-BulkJobNode-properties-inventory-properties-inventory-0)

  Title: `Inventory`

  Minimum Value: `1`
- [job:
  integer](#201-definitions-BulkJobNode-properties-job-properties-job-0)

  Title: `Job`
- [job\_slice\_count:
  integer](#201-definitions-BulkJobNode-properties-job_slice_count-properties-job_slice_count-0)

  Title: `Job slice count`

  Minimum Value: `0`
- [job\_tags:
  string](#201-definitions-BulkJobNode-properties-job_tags-properties-job_tags-0)

  Title: `Job tags`
- [job\_type:
  string](#201-definitions-BulkJobNode-properties-job_type-properties-job_type-0)

  Title: `Job type`

  Allowed Values: `[
  "run",
  "check"
  ]`
- [labels:
  array](#201-definitions-BulkJobNode-properties-labels-properties-labels-0)  [labels](#201-definitions-BulkJobNode-properties-labels)
- [limit:
  string](#201-definitions-BulkJobNode-properties-limit-properties-limit-0)

  Title: `Limit`
- [modified:
  string](#201-definitions-BulkJobNode-properties-modified-properties-modified-0)

  Title: `Modified`

  Read Only: `true`
- [related:
  string](#201-definitions-BulkJobNode-properties-related-properties-related-0)

  Title: `Related`

  Read Only: `true`
- [scm\_branch:
  string](#201-definitions-BulkJobNode-properties-scm_branch-properties-scm_branch-0)

  Title: `Scm branch`
- [skip\_tags:
  string](#201-definitions-BulkJobNode-properties-skip_tags-properties-skip_tags-0)

  Title: `Skip tags`
- [success\_nodes:
  array](#201-definitions-BulkJobNode-properties-success_nodes-properties-success_nodes-0)  [success\_nodes](#201-definitions-BulkJobNode-properties-success_nodes)

  Read Only: `true`

  Unique Items Required: `true`
- [summary\_fields:
  string](#201-definitions-BulkJobNode-properties-summary_fields-properties-summary_fields-0)

  Title: `Summary fields`

  Read Only: `true`
- [timeout:
  integer](#201-definitions-BulkJobNode-properties-timeout-properties-timeout-0)

  Title: `Timeout`
- [type:
  string](#201-definitions-BulkJobNode-properties-type-properties-type-0)

  Title: `Type`

  Read Only: `true`
- [unified\_job\_template(required):
  integer](#201-definitions-BulkJobNode-properties-unified_job_template-properties-unified_job_template-0)

  Title: `Unified job template`

  Minimum Value: `1`

  Primary key of the template for this job, can be a job template or inventory source.
- [url:
  string](#201-definitions-BulkJobNode-properties-url-properties-url-0)

  Title: `Url`

  Read Only: `true`
- [verbosity:
  string](#201-definitions-BulkJobNode-properties-verbosity-properties-verbosity-0)

  Title: `Verbosity`

  Allowed Values: `[
  "0",
  "1",
  "2",
  "3",
  "4",
  "5"
  ]`
- [workflow\_job:
  string](#201-definitions-BulkJobNode-properties-workflow_job-properties-workflow_job-0)

  Title: `Workflow job`

```
{
    "description":"List of jobs to be launched, JSON. e.g. [{\"unified_job_template\": 7}, {\"unified_job_template\": 10}]",
    "properties":{
        "all_parents_must_converge":{
            "description":"If enabled then the node will only run if all of the parent nodes have met the criteria to reach this node",
            "title":"All parents must converge",
            "type":"boolean",
            "x-nullable":true
        },
        "always_nodes":{
            "items":{
                "type":"integer"
            },
            "readOnly":true,
            "type":"array",
            "uniqueItems":true
        },
        "created":{
            "readOnly":true,
            "title":"Created",
            "type":"string"
        },
        "credentials":{
            "items":{
                "minimum":"1",
                "type":"integer"
            },
            "type":"array"
        },
        "diff_mode":{
            "title":"Diff mode",
            "type":"boolean",
            "x-nullable":true
        },
        "do_not_run":{
            "description":"Indicates that a job will not be created when True. Workflow runtime semantics will mark this True if the node is in a path that will decidedly not be ran. A value of False means the node may not run.",
            "title":"Do not run",
            "type":"boolean",
            "x-nullable":true
        },
        "execution_environment":{
            "minimum":"1",
            "title":"Execution environment",
            "type":"integer"
        },
        "extra_data":{
            "title":"Extra data",
            "type":"object"
        },
        "failure_nodes":{
            "items":{
                "type":"integer"
            },
            "readOnly":true,
            "type":"array",
            "uniqueItems":true
        },
        "forks":{
            "minimum":"0",
            "title":"Forks",
            "type":"integer",
            "x-nullable":true
        },
        "id":{
            "readOnly":true,
            "title":"ID",
            "type":"integer"
        },
        "identifier":{
            "description":"An identifier coresponding to the workflow job template node that this node was created from.",
            "maxLength":"512",
            "title":"Identifier",
            "type":"string",
            "x-nullable":true
        },
        "instance_groups":{
            "items":{
                "minimum":"1",
                "type":"integer"
            },
            "type":"array"
        },
        "inventory":{
            "minimum":"1",
            "title":"Inventory",
            "type":"integer"
        },
        "job":{
            "title":"Job",
            "type":"integer",
            "x-nullable":true
        },
        "job_slice_count":{
            "minimum":"0",
            "title":"Job slice count",
            "type":"integer",
            "x-nullable":true
        },
        "job_tags":{
            "title":"Job tags",
            "type":"string",
            "x-nullable":true
        },
        "job_type":{
            "enum":[
                "run",
                "check"
            ],
            "title":"Job type",
            "type":"string",
            "x-nullable":true
        },
        "labels":{
            "items":{
                "minimum":"1",
                "type":"integer"
            },
            "type":"array"
        },
        "limit":{
            "title":"Limit",
            "type":"string",
            "x-nullable":true
        },
        "modified":{
            "readOnly":true,
            "title":"Modified",
            "type":"string"
        },
        "related":{
            "readOnly":true,
            "title":"Related",
            "type":"string"
        },
        "scm_branch":{
            "title":"Scm branch",
            "type":"string",
            "x-nullable":true
        },
        "skip_tags":{
            "title":"Skip tags",
            "type":"string",
            "x-nullable":true
        },
        "success_nodes":{
            "items":{
                "type":"integer"
            },
            "readOnly":true,
            "type":"array",
            "uniqueItems":true
        },
        "summary_fields":{
            "readOnly":true,
            "title":"Summary fields",
            "type":"string"
        },
        "timeout":{
            "title":"Timeout",
            "type":"integer",
            "x-nullable":true
        },
        "type":{
            "readOnly":true,
            "title":"Type",
            "type":"string"
        },
        "unified_job_template":{
            "description":"Primary key of the template for this job, can be a job template or inventory source.",
            "minimum":"1",
            "title":"Unified job template",
            "type":"integer"
        },
        "url":{
            "readOnly":true,
            "title":"Url",
            "type":"string"
        },
        "verbosity":{
            "enum":[
                "0",
                "1",
                "2",
                "3",
                "4",
                "5"
            ],
            "title":"Verbosity",
            "type":"string",
            "x-nullable":true
        },
        "workflow_job":{
            "title":"Workflow job",
            "type":"string",
            "x-nullable":true
        }
    },
    "required":[
        "unified_job_template"
    ],
    "type":"object"
}
```

Nested Schema : always\_nodes

Type: `array`

Read Only: `true`

Unique Items Required: `true`

[Show Source](#)

- [Array of:
  integer](#201-definitions-BulkJobNode-properties-always_nodes-items-items-0)

```
{
    "items":{
        "type":"integer"
    },
    "readOnly":true,
    "type":"array",
    "uniqueItems":true
}
```

Nested Schema : credentials

Type: `array`

[Show Source](#)

- [Array of:
  integer](#201-definitions-BulkJobNode-properties-credentials-items-items-0)

  Minimum Value: `1`

```
{
    "items":{
        "minimum":"1",
        "type":"integer"
    },
    "type":"array"
}
```

Nested Schema : Extra data

Type: `object`

Title: `Extra data`

Nested Schema : failure\_nodes

Type: `array`

Read Only: `true`

Unique Items Required: `true`

[Show Source](#)

- [Array of:
  integer](#201-definitions-BulkJobNode-properties-failure_nodes-items-items-0)

```
{
    "items":{
        "type":"integer"
    },
    "readOnly":true,
    "type":"array",
    "uniqueItems":true
}
```

Nested Schema : instance\_groups

Type: `array`

[Show Source](#)

- [Array of:
  integer](#201-definitions-BulkJobNode-properties-instance_groups-items-items-0)

  Minimum Value: `1`

```
{
    "items":{
        "minimum":"1",
        "type":"integer"
    },
    "type":"array"
}
```

Nested Schema : labels

Type: `array`

[Show Source](#)

- [Array of:
  integer](#201-definitions-BulkJobNode-properties-labels-items-items-0)

  Minimum Value: `1`

```
{
    "items":{
        "minimum":"1",
        "type":"integer"
    },
    "type":"array"
}
```

Nested Schema : success\_nodes

Type: `array`

Read Only: `true`

Unique Items Required: `true`

[Show Source](#)

- [Array of:
  integer](#201-definitions-BulkJobNode-properties-success_nodes-items-items-0)

```
{
    "items":{
        "type":"integer"
    },
    "readOnly":true,
    "type":"array",
    "uniqueItems":true
}
```

[Back to Top](#top)