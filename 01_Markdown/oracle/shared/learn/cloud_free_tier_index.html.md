---
title: "Getting Started with Oracle Cloud Free Tier"
source_url: "https://docs.oracle.com/en/learn/cloud_free_tier/index.html"
fetched: 2026-03-26
tags:
  - "oracle-linux"
type: "oracle-doc"
sensitivity: public
---

# Get Started with Oracle Cloud Infrastructure Free Tier

## Introduction

Oracle Cloud Infrastructure (OCI) free tier provides a free time-limited promotional trial that allows you to explore a wide range of OCI products and a set of always free offers that never expire. You can use OCI free tier to try out one of our tutorials in an actual OCI environment.

### Objectives

- Sign up and sign in for OCI free tier account.
- Prepare your account so you can try one of our tutorials.

### Prerequisites

- For security purposes, most users will need a mobile phone number and a credit card to create an account. Your credit card will not be charged unless you upgrade your account.

## Sign up for Oracle Cloud Infrastructure Free Tier Account

1. Open a new browser window and go to the following URL: [Oracle Cloud Infrastructure](https://signup.oraclecloud.com/).
2. Follow the instructions to sign up for your free tier account.

   > **Note:** During sign up, select your home region carefully. You can provision Always Free Oracle Autonomous Databases only in your home region.

   When you finish signing up, you will be redirected to the Oracle Cloud Infrastructure sign in page. You will also get an email with your OCI free tier account credentials.

## Sign in to the Oracle Cloud Infrastructure Console

1. Open the email you received, and click the link for your new cloud account.
2. Sign in to the Oracle Cloud Infrastructure Console, using the credentials in the email.

   From the Oracle Cloud Infrastructure Console, you can access all the available Oracle Cloud Infrastructure services and track your usage.

## Launch Your Always Free Resources

Oracle offers you the ability to automatically create a full set of Always Free resources in a few minutes using the OCI Resource Manager serviceâs sample solutions feature. Solutions are pre-built Terraform configurations that help you easily create sets of resources used in common scenarios using a single, simple workflow.

When you provision your Always Free resources using the provided sample solution, your resources are created with the settings and configuration you need to start creating applications in the cloud. You donât need to have experience with Terraform to use the sample solution.

1. Log in into your Oracle Cloud Infrastructure account.
2. Open the navigation menu. Under **Developer Service**, go to **Resource Manager** and click **Stacks**.
3. Click **Create Stack**.
4. In the **Create stack** page, select **Template**.
5. In the **Stack configuration** section, click **Select template**.
6. In the **Browse template** page, click **Architecture** and select **Sample e-commerce application (MuShop Basic)**.
7. Click **Select template**.
8. (*Optional*) Enter the following information.

   - **Name:** Enter a name for the new stack. If you do not provide a name, a default name is provided on the server.
   - **Description:** Enter a description for the stack.
9. In **Create in compartment**, select a different compartment from your current compartment in which to create the stack.
10. (*Optional*) Click **Show advanced options** and assign tags to the stack.

    - **Tag namespace:** To add a defined tag, select an existing namespace. To add a free-from tag, leave the value blank.
    - **Tag key:** To add a defined tag, select an existing tag key. To add a free-form tag, type the key name that you want.
    - **Tag value:** Enter the tag value that you want.
    - **Add tag:** Click to add another tag.
11. Click **Next**.
12. In the **Configure variables** page, the variables displayed are auto-populated from the Terraform file that you uploaded. You do not need to change these variables if you are provisioning your Always Free resources using the Terraform file provided by Oracle and click **Next**.
13. In the **Review** page, verify your stack configuration and click **Create** to create your stack.

Your set of Always Free resources should take no more than a few minutes to provision.

## Related Links

- [Always Free Resources](https://docs.oracle.com/en-us/iaas/Content/FreeTier/resourceref.htm#Details_of_the_Always_Free_Resources)
- [Frequently Asked Questions](https://docs.oracle.com/en-us/iaas/Content/FreeTier/faq.htm)
- [Creating a Stack from a Template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-template.htm)

## Acknowledgments

- **Authors** - OHC Learn Publishing Team

## More Learning Resources

Explore other labs on [docs.oracle.com/learn](https://docs.oracle.com/learn) or access more free learning content on the [Oracle Learning YouTube channel](https://www.youtube.com/user/OracleLearning). Additionally, visit [education.oracle.com/learning-explorer](https://education.oracle.com/learning-explorer) to become an Oracle Learning Explorer.

For product documentation, visit [Oracle Help Center](https://docs.oracle.com).

---

[Title and Copyright Information](#copyright-information)

Get Started with Oracle Cloud Infrastructure Free Tier

F36509-06

February 2025

[Copyright Â©](https://docs.oracle.com/pls/topic/lookup?ctx=en/legal&id=cpyr)2024, Oracle and/or its affiliates.