---
title: "Accessibility User's Guide"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/8/accessibility"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "ol8"
  - "accessibility"
type: "oracle-doc"
sensitivity: public
---

Accessibility User's Guide

F30129-12

January 2024

---

[Title and Copyright Information](#copyright-information)

Oracle Linux 8 Accessibility User's Guide

F30129-12

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2020, 2024, Oracle and/or its affiliates.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/accessibility/accessibility-Preface.html -->

The [Oracle Linux 8: Accessibility User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/8/accessibility/) describes the accessibility
features that are available in the Oracle Linux operating system.

### Documentation License

The content in this document is licensed under the [Creative Commons Attribution–Share Alike 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (CC-BY-SA) license. In accordance with
CC-BY-SA, if you distribute this content or an adaptation of it, you must provide attribution
to Oracle and retain the original copyright notices.

### Conventions

The following text conventions are used in this document:

| Convention | Meaning |
| --- | --- |
| boldface | Boldface type indicates graphical user interface elements associated with an action, or terms defined in text or the glossary. |
| italic | Italic type indicates book titles, emphasis, or placeholder variables for which you supply particular values. |
| `monospace` | Monospace type indicates commands within a paragraph, URLs, code in examples, text that appears on the screen, or text that you enter. |

### Documentation Accessibility

For information about Oracle's commitment to accessibility, visit the Oracle Accessibility
Program website at <https://www.oracle.com/corporate/accessibility/>.

For information about the accessibility of the Oracle Help Center, see the Oracle
Accessibility Conformance Report at <https://www.oracle.com/corporate/accessibility/templates/t2-11535.html>.

### Access to Oracle Support for Accessibility

Oracle customers that have purchased support have access to electronic support through My
Oracle Support. For information, visit <https://www.oracle.com/corporate/accessibility/learning-support.html#support-tab>.

### Diversity and Inclusion

Oracle is fully committed to diversity and inclusion. Oracle respects and values having a
diverse workforce that increases thought leadership and innovation. As part of our
initiative to build a more inclusive culture that positively impacts our employees,
customers, and partners, we are working to remove insensitive terms from our products and
documentation. We are also mindful of the necessity to maintain compatibility with our
customers' existing technologies and the need to ensure continuity of service as Oracle's
offerings and industry standards evolve. Because of these technical constraints, our effort
to remove insensitive terms is ongoing and will take time and external cooperation.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/accessibility/accessibility-WorkingWithAccessibilityFeaturesinEnterpriseLinux.html -->

Accessibility features offer users with vision, hearing, and motor impairments ways to more
easily use the Oracle Linux desktop. This guide provides information about enabling and
configuring the accessibility features that are included in Oracle Linux 8.

### Selecting a Desktop Version

Oracle Linux8 offers both the Standard and
Classic GNOME desktop. When you install Oracle Linux by using the Server With GUI profile or
environment, the Standard GNOME desktop is selected by default. However, you can select
another desktop version if preferred.

To view the desktop versions or switch between versions, do the following:

1. Ensure that you're logged out of the Oracle Linux
   8 session.
2. Click the login username.
3. Click the cogwheel next to the Sign In button.

   The list of desktop versions is displayed.
4. (Optional) Select a desktop version.
5. Continue logging in to the server.

The desktop selection becomes a persistent setting and applies to all authorized users of
the system.

### About Assistive Technologies

Assistive technologies promote accessibility for users with
specific impairments.

Alternative presentations that are provided for these users
include the following:

- Synthesized speech
- Magnified content
- Alternative input methods
- Additional navigation methods
- Content transformations

Software features of Oracle Linux enable users with physical impairments
to use all of the functionality of the desktop. Various desktop tools also enable you to
customize the desktop's appearance and behavior.

Note:

Anaconda installation software for Oracle Linux
8  doesn't provide any accessibility features.

### Accessing Assistive Technologies

In Oracle Linux, the assistive technologies are listed on the Universal Access
panel of the GNOME desktop's Settings window. Accessing the panel differs slightly
between Standard and Classic desktops. However, the feature descriptions and configuration
procedures are the same for both. This document assumes that you're using the default
(Standard) desktop on the system.

#### Using the Standard Desktop

Choose one of the following methods:

- Accessing through the System
  Tools group icon

  The System Tools group icon consists of the 3 icons at the right side of the top
  bar of the screen. See the icons boxed in red in [Figure 1-1](accessibility-WorkingWithAccessibilityFeaturesinEnterpriseLinux.html#quick-access__quick-access-menu).

  1. On the right side of the top bar, click
     System Tools.
  2. Click Settings.
  3. From the list of options on the left panel, select Universal
     Access.
- Accessing through the
  Activities menu option

  1. On the top bar, click
     Activities.
  2. On the search field, type `universal
     access`.
  3. From the list of options on the left panel, select Universal
     Access.
- Accessing through the command line

  1. Select the Terminal icon at the bottom of the screen.

     If the icon isn't visible, click Activities, then select the icon.
  2. On the terminal window, type:

     ```
     gnome-control-center universal-access
     ```
  3. From the list of options on the left panel, select Universal
     Access.

#### Using the Classic Desktop

Choose one of the following methods:

- Accessing through the System
  Tools group icon

  The System Tools group icon consists of the 3 icons at the right side of the top
  bar of the screen. See the icons boxed in red in [Figure 1-1](accessibility-WorkingWithAccessibilityFeaturesinEnterpriseLinux.html#quick-access__quick-access-menu).

  1. On the right side of the top bar, click
     System Tools.
  2. Click Settings.
  3. From the list of options on the left panel, select Universal
     Access.
- Accessing through the
  Applications menu
  option

  1. On the top bar, click Applications, select System
     Tools, then select Settings.
  2. From the list of options on the left panel, select Universal
     Access.
- Accessing through the command line

  1. On the top bar, click Applications, select Favorites, then select
     Terminal.
  2. Type the following
     command:

     ```
     gnome-control-center universal-access
     ```
  3. From the list of options on the left panel, select Universal
     Access.

#### Configuring Quick Access

Oracle Linux provides a Universal Access
Menu, which enables you to
access and configure accessibility features without the need to open the Universal Access panel. This menu
is disabled by default. To make the menu available, open the Universal
Access panel and set the Always Show Universal Access Menu switch to On. Toggling this switch makes the Universal Access Menu icon become permanently visible on the top bar of the desktop.

Clicking the icon opens a list of accessibility features, as shown in the following
figure:

Figure 1-1 Desktop Accessibility Features

Note:

Enabling selected features in the Universal Access panel also automatically enables quick access,
even if the Always Show Universal Access Menu switch is disabled. However, in
this case, if you switch off all of the enabled features through quick access, then the
quick access icon disappears from the top bar.

Toggling the Always Show Universal Access Menu switch ensures that quick access
is available permanently regardless of whether assistive features are enabled or not.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/accessibility/accessibility-OverviewofAccessibilityFeatures.html -->

In the GNOME desktop, features for aiding users with impairments are configured from the Universal Access
panel.

On the panel, accessibility features are listed according to
groups.

- Seeing

  Includes accessibility features and options for users with visual impairments. You can
  enable and customize the following settings:

  High Contrast
  :   Adjusts the contrast of windows and buttons on-screen so
      they are more or less vivid.

  Large Text
  :   Enlarges the font so that it's more readable.

  Cursor Size
  :   Increases and decreases the mouse cursor size.

  Zoom
  :   Magnifies text so that it's more readable.

  Screen Reader
  :   Reads aloud screen content to supplement visual reading.
      For details, see
      [Configuring the Screen Reader](accessibility-CustomizingAccessibilityFeatures.html#conf-screenreader).

  Sound Keys
  :   Beeps when the `Num Lock` or
      `Caps Lock` key is turned on or off.
- Hearing

  Includes the Visual Alerts option to aid those with hearing impairments. When
  enabled, the option provides a visual indication when an alert sound occurs. Available
  options include: Flash the window title and Flash the entire screen.
- Typing

  Includes accessibility features and options for users with mobility impairments. You can
  enable and customize the following settings:

  Screen Keyboard
  :   Enables desktop navigation and application use without a
      physical keyboard.

  Repeat Keys
  :   Specifies that the keyboard not repeat letters when a
      key is held down. This setting also enables you to
      change the delay and speed of repeat keys.

  Cursor Blinking
  :   Causes the cursor to blink in text fields when enabled.

  Typing Assist (AccessX)
  :   Opens a submenu that contains more keyboard settings. For details, see [Configuring Typing Assist](accessibility-CustomizingAccessibilityFeatures.html#conf-typeassist).
- Pointing & Clicking

  Includes accessibility features and options for users with motor impairments that render
  using a mouse or any pointing device difficult.

  Mouse Keys
  :   Enables you to control the mouse pointer by using the
      numeric keypad on your keyboard.

  Click Assist
  :   Opens a submenu that contains more settings for clicking the mouse. For details,
      see [Configuring Click Assist](accessibility-CustomizingAccessibilityFeatures.html#conf-clickassist).

  Double-Click Delay
  :   Enables you to adjust the length of time to delay the
      double-click action.

For more information about universal access in the GNOME desktop, go to <https://help.gnome.org/users/gnome-help/stable/a11y.html>.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/accessibility/accessibility-CustomizingAccessibilityFeatures.html -->

Accessibility features already have preconfigured settings so that they're immediately
usable after an Oracle Linux installation. However, some of these features
can be customized according to preferences. This chapter describes these features that you can
further enhance. When you enable a feature after reconfiguring it, the new settings are
applied.

### Configuring the Screen Reader

Oracle Linux provides Orca as its default on-screen reader. The
`orca` package is installed on the Oracle Linux
8 system by default. When enabled, the Orca
screen reader speaks text as you move the focus of the cursor on-screen.

Configurable Settings of the Screen Reader

The Screen Reader Preferences window contains the following tabs, each of which has
a list of customizable settings:

General
:   Configures how Orca behaves.

Voice
:   Determines the voice that Orca uses when reading the screen.

Speech
:   Defines what the reader reads aloud and the degree of verbosity.

Braille
:   Configures Orca Braille display support.

Key Echo
:   Defines what the reader reads aloud while you type.

Key Bindings
:   Defines keyboard shortcuts for Orca.

Pronunciation
:   Configures word pronunciation.

Text Attributes
:   Configures text formatting.

Customizing the Screen Reader

1. Type the following command:

   ```
   orca -s
   ```

   The `-s` option can also be typed as `--setup`. The
   command opens the Screen Reader Preferences window.
2. Customize the reader according to specific needs.

   Click each tab to configure the different options on those tabs.

   For Braille configuration, see [Using Braille](accessibility-UsingBraille.html#chap-braille).

   Note:

   When you open the Screen Reader Preferences window, the screen reader is
   temporarily enabled and any action you perform on the desktop is read aloud. When you
   exit the window, the screen reader is switched off.
3. Click Apply, then click OK.
4. At the command line, press Ctrl-C to return to the command prompt.
5. Enable the screen reader by using either the Universal
   Access panel or, if available,
   the quick access icon on the desktop's top bar.

### Configuring the Magnifier

Zoom is the default magnifier that's included in the GNOME desktop for Oracle Linux
8.

Configurable Settings of the Magnifier

The Zoom Options window contains the following tabs, each of which has a list of
customizable settings:

Magnifier
:   Configures magnification and magnifier cursor behavior.

Crosshairs
:   Configures cross hair appearance, including color.

    Note that to use Crosshairs, you would need to toggle the feature's switch on
    this tab to ON. However, the crosshairs appear only if you also enable Zoom.

    To use the magnifier but not the crosshairs, you would need to return to this window
    to disable the feature.

Color Effects
:   Configures the display of colored content.

Customizing the Magnifier

1. Access the Universal Access panel by using a preferred method.

   See [Accessing Assistive Technologies](accessibility-WorkingWithAccessibilityFeaturesinEnterpriseLinux.html#ol-assistive-gnome).
2. From the list of options on the panel, select Zoom.

   The Zoom Options window is displayed.
3. Customize the magnifier according to your preferences.

   Click each tab to configure the different options on those tabs.
4. (Optional) Toggle the magnifier
   switch to ON to use the feature immediately.

   You can also enable the magnifier later through the Universal
   Access Menu icon on the
   desktop's top bar.

For more information about customizing the magnifier, go to <https://help.gnome.org/users/gnome-help/stable/a11y-mag.html.en>.

### Configuring Typing Assist

Typing Assist consists of several assistive technologies for using the keyboard.

Configurable Settings of Typing Assist

Typing Assist is one of the features under the Typing group. The settings
include the following:

Enable By Keyboard
:   Enables keyboard control to navigate the desktop instead of using a mouse.

    For help with using keyboard navigation, see <https://help.gnome.org/users/gnome-help/stable/shell-keyboard-shortcuts.html.en>.

Sticky Keys
:   Enables shortcut keys to be typed in sequence instead of one key being held before
    the other key is pressed.

Slow Keys
:   Controls the delay between a key being typed and the corresponding character being
    displayed on-screen.

Bounce Keys
:   Enables ignoring fast and repetitive pressing of keys.

Except for Enable By Keyboard, the settings can be enabled through the Universal Access Menu icon on the desktop's top bar.

Customizing Typing Assist

1. Access the Universal Access panel by using a preferred method.

   See [Accessing Assistive Technologies](accessibility-WorkingWithAccessibilityFeaturesinEnterpriseLinux.html#ol-assistive-gnome).
2. Under the Typing group, select Typing Assist (AccessX) .

   The Typing Assist window is displayed.
3. Customize the settings for key behavior according to your preferences.

For more information about customizing Typing Assist, go to <https://help.gnome.org/users/gnome-help/stable/keyboard.html.en>.

### Configuring Click Assist

Click Assist consists of several assistive technologies for using the mouse or other
pointing devices.

Configurable Settings of Click Assist

Click Assist is one of the features under the Point & Clicking group. The
settings include the following:

Simulated Secondary Click
:   Triggers a secondary click when you hold the primary button, which causes the
    equivalent action of double-clicking.

Hover Click
:   Triggers a click when you hover over a specific screen location, which causes the
    equivalent action of clicking or selecting.

Customizing Click Assist

1. Access the Universal Access panel by using a preferred method.

   See [Accessing Assistive Technologies](accessibility-WorkingWithAccessibilityFeaturesinEnterpriseLinux.html#ol-assistive-gnome).
2. Under the Pointing & Clicking group, select Click Assist.

   The Click Assist window is displayed.
3. Customize the settings for mouse click behavior according to set preferences.

For more information about configuring Click Assist, go to <https://help.gnome.org/users/gnome-help/stable/mouse.html.en>.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/8/accessibility/accessibility-UsingBraille.html -->

Braille support is included in the GNOME desktop's accessibility features. Likewise, the
`brltty` daemon that's running as a background process enables users to
access information on Braille display devices.

### Configuring Braille Options on the Screen Reader

The GNOME desktop's Screen Readers Preference window contains a page for Braille
configuration.

Configurable Braille Settings on the Screen Reader

On the Braille page, you can configure the following settings:

Display Settings
:   Defines how Braille is displayed.

Verbosity
:   Determines the amount of information that is rendered in Braille.

Selection and Hyperlink Indicators
:   Defines how selected text and hyperlinks are displayed.

Flash Message Settings
:   Enables notifications and configures how these notifications are handled.

For more information about configuring Orca's Braille options, go to <https://help.gnome.org/users/orca/stable/preferences_braille.html.en>.

Customizing Braille on the Screen Reader

1. Type the following command:

   ```
   orca -s
   ```

   The `-s` option can also be typed as `--setup`. The
   command opens the Screen Reader Preferences window.
2. Click the Braille tab.
3. Customize the Braille options according to user needs.
4. Enable the screen reader by using either the Universal
   Access panel or, if available,
   the quick access icon on the desktop's top bar.

Note:

If you change settings in `/etc/brltty.conf`, then you must also restart
Orca. To configure `/etc/brltty.conf`, see [Configuring the BRLTTY Service](accessibility-UsingBraille.html#brltty).

### Configuring the BRLTTY Service

Support for a Braille device is provided by the BRLTTY daemon
(`brltty`). You configure this service through the
`/etc/brltty.conf` configuration file.

Note:

The `brltty` service isn't available by default. To use this service you
must install the `brltty` package.

Configurable Settings of the brltty Service

The following are a selection of configurations that you can set in
`/etc/brltty.conf`:

- Authorize users who can use the Braille device.

  Specify the users on the line `#api-parameters Auth=user:`, for
  example:

  ```
  api-parameters Auth=user:jsmith, jdoe, bbrown
  ```
- Authorize groups who can use the Braille device.

  Specify the groups on the line `#api-parameters Aut=group:`. For
  example, for a group called `braille`, you would enter:

  ```
  api-parameters Auth=group:braille
  ```
- Indicate the Braille display device driver.

  Uncomment the appropriate `#braille-driver` line that contains your
  selected driver. Drivers are identified by two-letter codes, which are provided in the
  configuration file, for example:

  ```
  braille-driver vo
  ```

  On a single `braille-driver` line, you can specify multiple,
  comma-separated drivers. In this case, the service automatically scans the list and
  detects the appropriate driver.
- Indicate the type of Braille display device.

  Uncomment the appropriate `#braille-device` line that contains your
  selected device. Several lines that correspond to specific device types are provided,
  for example:

  ```
  braille-device bluetooth:address
  ```

  On a single `braille-device` line, you can specify multiple,
  comma-separated devices. In this case, the service automatically scans the list and
  detects the appropriate device.

Using the brltty Service

1. Install the `brltty` package.

   ```
   sudo dnf install -y brltty
   ```
2. Configure settings in `/etc/brltty.conf` as needed.
3. Enable the `brltty` service.

   ```
   sudo systemctl enable brltty
   ```
4. If prompted, type the user password.
5. Reboot the system.
6. After the system reboots, verify that the service is running, as follows:

   ```
   sudo systemctl status brltty
   ```

   ```
   * brltty service - Braille display driver for Linux/Unix
      Loaded: loaded (/usr/lib/systemd/system/brltty.service; enabled; vendor preset: disabled
      Active: active (running) since Wed 2020-04-15 12:07:48 PDT; 25min ago
   ...
   ```

Note:

If you change settings in `/etc/brltty.conf`, then you must also restart
Orca. To configure Braille options in the Screen Reader, see [Configuring Braille Options on the Screen Reader](accessibility-UsingBraille.html#braille-screenrdr).

For more information, see the `brltty(1)` manual page.