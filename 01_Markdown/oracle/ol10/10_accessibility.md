---
title: "Accessibility User's Guide"
source_url: "https://docs.oracle.com/en/operating-systems/oracle-linux/10/accessibility"
fetched: 2026-03-26
tags:
  - "oracle-linux"
  - "ol10"
  - "accessibility"
type: "oracle-doc"
sensitivity: public
---

## Oracle Linux 10

Accessibility User's Guide

G14600-03

September 2025

---

[Title and Copyright Information](#copyright-information)

Oracle Linux 10 Accessibility User's Guide

G14600-03

[Copyright ©](/pls/topic/lookup?ctx=en/legal&id=cpyr)2025, Oracle and/or its affiliates.

Documentation License

The content in this document is licensed under the (CC-BY-SA) license. In accordance with
CC-BY-SA, if you distribute this content or an adaptation of it, you must provide attribution
to Oracle and retain the original copyright notices.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/accessibility/accessibility-Preface.html -->

## Preface

The [Oracle Linux 10: Accessibility User's Guide](https://docs.oracle.com/en/operating-systems/oracle-linux/10/accessibility/) describes the accessibility
features that are available in the Oracle Linux operating system.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/accessibility/accessibility-WorkingWithAccessibilityFeaturesinEnterpriseLinux.html -->

## 1 Working With Accessibility Features in Oracle Linux

Accessibility features offer users with vision, hearing, and motor impairments ways to more
easily use the Oracle Linux desktop. This guide provides information about enabling and
configuring the accessibility features that are included in Oracle Linux 10.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/accessibility/accessibility-SelectingaDesktopVersion.html -->

## Selecting a Desktop Version

By default, when you install Oracle Linux
10 by using the Server With GUI profile or environment, the GNOME
desktop is installed. However, you can install additional desktop environments. For example,
to install GNOME classic, you can run the following command:

```
sudo dnf install gnome-classic-session
```

If more than one desktop is present on a system, you can select the one to
use when signing in, as shown in the following procedure.

Changes to the desktop selection are a persistent setting and apply to all authorized users
of the system.

To view the desktop environments or switch between environments, do the following:

1. Log out of any existing Oracle Linux desktop environments.

   The Log on page appears.
2. Select the login username.
3. Select the Choose Desktop "cogwheel" icon  at the
   bottom right of the screen.

   Note:

   The Choose Desktop icon is only present if more than one
   desktop environment is installed.

   A list of available desktop options appears.
4. (Optional) Select a desktop environment.
5. Continue logging in to the server.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/accessibility/accessibility-AboutAssistiveTechnologies.html -->

## About Assistive Technologies

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
to use all the functionality of the desktop. Various desktop tools also enable you to
customize the desktop's appearance and behavior.

Note:

Anaconda installation software for Oracle Linux doesn't provide any accessibility features.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/accessibility/accessibility-AccessingAssistiveTechnologies.html -->

## Accessing Assistive Technologies

In Oracle Linux, GNOME settings are displayed and configured using a
graphical application called the GNOME Control Center. The GNOME Control Center
displays the accessibility settings on the Accessibility
panel of the Settings window. The following image shows an example of
the Accessibility panel:

Figure 1-1 Accessibility panel in the GNOME Control Center Settings
Window

Accessing the panel differs slightly between GNOME and GNOME Classic desktops. However, the feature
descriptions and the available configurations are the same for both. Unless otherwise stated,
this document assumes that you're using the default (GNOME) desktop on the system.

The following sections show different ways of accessing the Accessibility panel of the Settings window.

### Using the GNOME Desktop

Choose one of the following methods:

- Accessing through the System Tools group icon

  The System Tools group icon consists of 3 icons at the right side
  of the top bar of the screen. The following image shows an example of a System tools group
  icon highlighted in a yellow box:


  1. On the right side of the top bar, select the System Tools
     group icon.

     A panel of options appears.
  2. Select the Settings option.

     The GNOME control center appears.
  3. From the list of options on the left panel, select Accessibility.

     The accessibility options appear in the right panel.
- Accessing through the Activities
   workspace indicator

  The Activities workspace indicator is at the left
  side of the top bar of the screen. The following image shows an
  Activities workspace indicator highlighted in a yellow box:


  1. On the top bar, select the Activities workspace indicator.

     A search field appears.
  2. In the search field, type `accessibility`.

     An option to display the Accessibility settings
     appears.
  3. Select the option to display the Accessibility settings.

     The GNOME control centre opens displaying the Accessibility options.
- Accessing through the command line

  1. On the top bar, select the Activities workspace indicator.

     A bar of application icons (called the dash)
     appears.
  2. From the dash, select the terminal icon.
  3. In the terminal window, type:

     ```
     gnome-control-center universal-access
     ```

     The GNOME control centre opens displaying the Accessibility options.

### Using the GNOME Classic Desktop

Choose one of the following methods:

- Accessing through the System Tools group icon

  The System Tools group icon consists of the 3 icons at the right
  side of the top bar of the screen. The following image shows an example of a System tools group
  icon highlighted in a red box:


  1. On the right side of the top bar, select the System Tools
     group icon.

     A panel of options appears.
  2. Select Settings option.

     The GNOME control center appears.
  3. From the list of options on the left panel, select Accessibility.

     The accessibility options appear in the right panel.
- Accessing through the Apps menu option

  1. On the top bar, select Apps.

     A menu with a list of options appears.
  2. From the menu, select System Tools.

     A list of System Tools options appears.
  3. From the options of System Tools , select
     Settings.

     The GNOME control center appears.
  4. From the list of options on the left panel, select Accessibility.

     The accessibility options appear in the right panel.
- Accessing through the command line

  1. On the top bar, select Apps.

     A menu with a list of options appears.
  2. From the options, select Favorites, and then select
     Terminal.
  3. Type the following
     command:

     ```
     gnome-control-center universal-access
     ```

     The GNOME
     control centre opens displaying the Accessibility options.

### Configuring Quick Access

Oracle Linux provides an Accessibility
Menu, which enables you to access and configure accessibility features
without the need to open the Accessibility
panel. This menu is disabled by default. To make the menu available, open the Accessibility panel and set the Always Show Accessibility Menu switch to
On. Toggling this switch to the On position
makes the Accessibility Menu icon become permanently visible on the top bar of the
desktop.

Selecting the icon opens a list of accessibility features, as shown in the following
figure:

Figure 1-2 Desktop Accessibility Features

Note:

Enabling selected features in the Accessibility panel also automatically enables quick
access, even if the Always Show Accessibility Menu switch is disabled.
However, in this case, if you switch off all of the enabled features through quick access,
then the quick access icon disappears from the top bar.

Toggling the Always Show Accessibility Menu switch to the
On position ensures that quick access is available permanently,
regardless of whether assistive features are enabled or not.

### Viewing GNOME Help

You can get more information on configuring accessibility options in GNOME desktops by
viewing the GNOME Help pages.

Note:

Viewing GNOME help pages requires a web browser to be
installed on the system.

To view the GNOME Help pages, perform the following steps:

1. Access the GNOME control centre by following one of the procedures described in [Using the GNOME Desktop](accessibility-AccessingAssistiveTechnologies.html#standard-desktop) or [Using the GNOME Classic Desktop](accessibility-AccessingAssistiveTechnologies.html#classic-desktop)
2. From the list of options on the left panel, select Accessibility.
3. Do one of the following:

   - Press the F1 key.
   - Alternatively, if you prefer using the UI, select the
     Menu

     icon and then select Help.

   The GNOME Accessibility help pages are
   displayed in a web browser.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/accessibility/accessibility-OverviewofAccessibilityFeatures.html -->

## 2 Overview of Accessibility Features

In the GNOME desktop, features for aiding users with impairments are configured from the Accessibility panel.

When the Accessibility panel initially appears, it includes the following
options to display different types of accessibility settings:

- Seeing
- Hearing
- Typing
- Pointing and Clicking
- Zoom

An overview of the accessibility settings each of the preceding options
displays is provided in the following list:

- Seeing

  Selecting this option displays accessibility features for users with visual impairments.
  The settings you can enable and customize include the following:

  Screen Reader
  :   Reads aloud screen content to supplement visual reading. For details, see [Customizing the Screen Reader](accessibility-ConfiguringtheScreenReader.html#conf-orca "Customize the screen reader settings in the Screen Reader Preferences window.").

  High Contrast
  :   Adjusts the color contrast of windows and buttons on-screen so they're more or
      less vivid.

  On/Off Shapes
  :   Sets whether to use shapes to indicate state in addition to or instead of
      color.

  Animation Effects
  :   Toggles whether to use animation effects throughout the interface.

      Note:

      Turning off animation effects can result in more sudden visual transitions when
      UI elements change. This might have a negative impact on some visual
      sensitivities.

  Large Text
  :   Enlarges the font so that it's more readable.

  Cursor Size
  :   Increases and decreases the mouse cursor size.

  Sound Keys
  :   Beeps when the `Num Lock` or `Caps Lock`
      key is turned on or off.

  Always Show Scrollbars
  :   Sets the scrollbars to always be visible.
- Hearing

  Selecting this option displays accessibility features to aid users with hearing
  impairments. This includes the Visual Alerts setting that can be
  enabled to provide an onscreen flash when an alert sound occurs. Available options for
  defining the Flash Area include Entire
  Window and Entire Screen.
- Typing

  Selecting this option displays accessibility features for users with mobility
  impairments. The settings you can enable and customize include the following:

  Screen Keyboard
  :   Enables desktop navigation and application use without a physical keyboard.

  Text Cursor settings
  :   The Text Cursor settings include Cursor Blinking and
      Blink Speed. Enabling the Cursor
      Blinking setting causes the cursor to blink in text fields and
      Blink Speed setting can be used to control the blink
      frequency.

  Typing Assist settings
  :   The Typing Assist settings group includes the following settings for keyboard keys:

      - Repeat Keys
      - Sticky Keys
      - Slow Keys
      - Bounce Keys

      For more information on these settings, see [Customizing Typing Assist](accessibility-ConfiguringTypingAssistValues.html#conf-typeassistvalues "Customize the Typing Assist group configurations of the Typing settings that provide accessibility features, such as sticky keys and bounce keys, to help with key presses.").
- Pointing & Clicking

  Selecting this option displays accessibility features to aid users with motor impairments
  that make using a mouse or any pointing device difficult. The settings you can enable and
  customize include the following:

  Mouse Keys
  :   Enabling this setting lets you control the mouse pointer by using the numeric
      keypad on your keyboard.

  Locate Pointer
  :   Enables you to find the position of the mouse pointer on the screen by pressing the
      left control key.

  Activate Windows on Hover
  :   Enables you to place the mouse pointer over a window to activate it.

  Double-Click Delay
  :   Enables you to control how quickly you need to press the mouse button a second time
      to complete a double-click.

  Click Assist Settings
  :   The Click Assist settings group includes the following settings for the mouse:

      - Simulated Secondary Click

        Enables you to perform a secondary click (usually the right mouse button) by
        holding down the primary button for a length of time and then releasing it. The
        length of time for which you need to hold the primary button down before
        releasing it can be adjusted through the Acceptance Delay
        setting.
      - Hover Click

        Enables you to perform a mouse click by hovering the mouse pointer over the
        item to be clicked. The mouse does not have to be kept perfectly still while
        hovering the pointer as some movement is allowed. You can adjust the
        Motion Threshold setting to change the amount a mouse
        pointer can move and still be considered to be hovering.

      For more information on using these settings, see [Customizing Click Assist](accessibility-ConfiguringClickAssistValues.html#conf-clickassist-values "Customize the Click Assist group configurations of the Point & Clicking settings that provide accessibility features for using mouse pointer devices.").
- Zoom

  Selecting this option displays features for configuring different types of zoomed views,
  for example:

  - A zoomed view that uses the entire screen.
  - A zoomed square "magnifying lens" view that follows the mouse pointer.

  The zoomed views can be further enhanced by adjusting color and contrast settings and
  crosshair lines for the mouse pointer.

  Examples of settings include Desktop Zoom,
  Magnification Factor, Magnification View,
  Brightness, and Contrast.

  For a more complete list of settings and information on how to use them to configure
  zoomed views, see [Customizing Zoom](accessibility-ConfiguringZoom.html#conf-zoom "Enable Desktop Zoom and configure different types of zoomed views.")


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/accessibility/accessibility-CustomizingAccessibilityFeatures.html -->

## 3 Customizing Accessibility Features

Accessibility features already have preconfigured settings so that they're immediately
usable after an Oracle Linux installation. However, some of these features
can be customized according to preferences. This chapter provides an overview and examples of
how you can do this.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/accessibility/accessibility-ConfiguringtheScreenReader.html -->

## Customizing the Screen Reader

Customize the screen reader settings in the Screen Reader
Preferences window.

Oracle Linux provides Orca as its default on-screen reader. The
`orca` package is installed on the Oracle Linux
10 system by
default. When enabled, the Orca screen reader speaks text as you move the focus of the
cursor on-screen. This topic describes how to customize the screen reader configuration.

Note:

You must perform the following steps as a non-root user.

1. Run the `orca` command with the setup option to open the preferences
   window.

   Run the following command:

   ```
   orca -s
   ```

   The `-s` option can also be typed as `--setup`. The
   command opens the Screen Reader Preferences window.

   Note:

   When you open the Screen Reader Preferences window, the screen
   reader is temporarily enabled so you can hear the effect each setting has. The
   temporary activation of the screen reader is disabled when you close the window and
   end the program by pressing `Ctrl+C`.
2. Customize the reader according to specific needs. 

   Select each tab to configure the different options on those tabs. To
   see an overview of the available tabs see [Configurable Settings of the Screen Reader](accessibility-ConfiguringtheScreenReader.html#config-settings-orcavalues "The following table provides an overview of the different tabs of the Screen Reader Preferences and the types of settings each tab provides. For more details, view the Orca help pages by selecting the Help option on the Screen Reader Preferences window (viewing the help pages requires a web browser).")

   For Braille configuration, see [Using Braille](accessibility-UsingBraille.html#chap-braille).
3. Select Apply, then Select OK.
4. At the command line, press `Ctrl+C` to return to the command
   prompt.

   The temporary activation of the screen reader is disabled.
5. (Optional) Enable the screen reader.

   Access the Accessibility panel by using a
   preferred method. See [Accessing Assistive Technologies](accessibility-AccessingAssistiveTechnologies.html#ol-assistive-gnome)

   Select Seeing, and then switch the
   Screen Reader toggle to ON to enable the
   screen reader.

### Configurable Settings of the Screen Reader

The following table provides an overview of the different tabs of the Screen
Reader Preferences and the types of settings each tab provides. For more details,
view the Orca help pages by selecting the Help option on the
Screen Reader Preferences window (viewing the help pages requires a web
browser).

Table 3-1 Screen Reader Settings Tabs

| Tab Name | Description |
| --- | --- |
| General | Contains settings for general preferences, for example:   - The keyboard layout to use: Desktop (default) or   Laptop. - Mouse settings to use, for example whether Orca should present tooltips that   appear when the mouse hovers. - Settings to configure how progress bar updates are reported. |
| Voice | Contains voice settings. For example:   - The Voice type list of options, such as   Default, Uppercase and   Hyperlink, to configure different voices for different   types of text. - Global Voice Settings such as and Speak   multicase strings as words and Speak numbers as   digits. |
| Speech | Contains settings to define what the reader reads aloud and the degree of verbosity. The tab also contains settings for punctuation levels. |
| Braille | Configures Orca Braille display support. See [Configurable Braille Settings on the Screen Reader](accessibility-ConfiguringBrailleOptionsontheScreenReader.html#section_nhl_z1v_t5b) for an overview of available settings. |
| Echo | Defines what the reader reads aloud while you type. |
| Key Bindings | Defines keyboard shortcuts for Orca. |
| Pronunciation | Configures word pronunciation. |
| Text Attributes | Configures text formatting. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/accessibility/accessibility-ConfiguringZoom.html -->

## Customizing Zoom

Enable Desktop Zoom and configure different types of zoomed
views.

Customize Zoom settings to create a zoom view to suit the
needs of a specific user. The different types of magnified views you can configure
include the following:

- A full screen magnification view where the entire screen is magnified.
- A zoomed square "magnifying lens" view that follows the mouse pointer.
- A split screen view where half the screen, for example the bottom half,
  renders the magnified view of the mouse pointer location, whilst the other
  half displays the desktop without zoom settings.

The zoomed views can be further enhanced by adjusting color and contrast settings and
crosshair lines for the mouse pointer.

The following example procedure assumes you're configuring Zoom to render the
magnified view in the bottom half of the screen with thick blue crosshair lines to
help make the mouse pointer location more visible:

1. Access the Accessibility panel by using
   a preferred method. 

   See [Accessing Assistive Technologies](accessibility-AccessingAssistiveTechnologies.html#ol-assistive-gnome).
2. Select Zoom.

   A panel of Zoom options appears.
3. On the panel of Zoom options, in the Magnifier section, set the
   Magnification Factor to the required value, for example 1.50.
4. From the Magnifier View list, select Screen
   Area.

   Options for configuring the Screen Area become
   available.
5. From the Screen Area list, select Bottom
   Half.
6. In the Crosshairs section, switch the
   Crosshair Lines toggle to
   ON.

   Further Crosshair settings appear.
7. Use the Thickness slider to increase the thickness of
   the crosshair lines.
8. Select the Color setting.

   A list of colors appears on a panel.
9. From the panel of colors, select a color, for example, blue.
10. (Optional) Toggle the Desktop Zoom switch to
    ON to use the feature immediately.

    You can also enable the magnifier later through the Accessibility Menu icon
    on the desktop's top bar.

For more information about customizing the magnifier, see the following:

- GNOME help pages (see [Viewing GNOME Help](accessibility-AccessingAssistiveTechnologies.html#viewing-gnome-help) for information on how to
  view the help pages).
- [Configurable Settings for Zoom](accessibility-ConfiguringZoom.html#config-settings-zoom "The following tables provide an overview of different types of settings that can be configured for the zoom functionality.")
- <https://help.gnome.org/users/gnome-help/stable/a11y-mag.html.en>

### Configurable Settings for Zoom

The following tables provide an overview of different types of settings that can be
configured for the zoom functionality.

Table 3-2
Desktop Zoom

| Setting | Description |
| --- | --- |
| Desktop Zoom | Desktop Zoom sets whether Zoom functionality in the GNOME desktop is enabled. All other settings on the Zoom panel only come into effect if Desktop Zoom is enabled. |

Table 3-3 Magnifier Settings

| Setting | Description |
| --- | --- |
| Magnification Factor | This can be set to any value between 1.00 and 20.00. |
| Magnification View | The possible values for Magnification View are as follows:   - Follow Mouse Cursor: Creates a zoomed   square "magnifying lens" view that follows the mouse   pointer. - Screen Area: Stipulates that a dedicated   screen area, for example, the right half of the screen, is used   to render the magnified content. The location of the dedicated   screen area is defined in a separate Screen   Area setting. |
| Screen Area | This setting is used when Magnification View has been set to use a fixed screen region for the zoomed view.  The Screen Area setting can be set to one of the following:  - Full Screen: Magnifies the entire   screen. - Top Half: Renders magnified content   in top half of the screen. - Bottom Half: Renders magnified   content in bottom half of the screen. - Left Half: Renders magnified content   in left half of the screen. - Right Half: Renders magnified content   in right half of the screen. |

Table 3-4 Crosshairs Settings

| Setting | Description |
| --- | --- |
| Crosshair lines | Sets whether to use crosshairs in the magnified view to mark the cursor location. |
| Overlap Mouse Cursor | When selected, the crosshairs fully intersect and extend into the mouse cursor location. When unselected, the crosshairs end before they intersect the mouse cursor. |
| Thickness | Sets the thickness of the crosshair lines. |
| Length | Sets the length of the crosshair lines. |
| Color | Sets the color of the crosshair lines. |

Table 3-5 Color Filters Settings

| Setting | Description |
| --- | --- |
| Inverted | Inverts the screen colors in the magnified view. |
| Brightness | Sets screen brightness in the magnified view. |
| Contrast | Sets screen contrast in the magnified view. |
| Color | Sets color saturation the magnified view. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/accessibility/accessibility-ConfiguringClickAssistValues.html -->

## Customizing Click Assist

Customize the Click Assist group configurations of the Point &
Clicking settings that provide accessibility features for using mouse pointer
devices.

The Click Assist feature includes the Simulated
Secondary Click and Hover Click settings. The following
example procedure provides the steps you need to perform to enable and customize the
Simulated Secondary Click settings.

1. Access the Accessibility panel by using a preferred
   method. 

   See [Accessing Assistive Technologies](accessibility-AccessingAssistiveTechnologies.html#ol-assistive-gnome).
2. Select Pointing & Clicking.

   The Pointing & Clicking panel of options
   appears.
3. On the Pointing & Clicking panel, in the
   Click Assist section, switch the
   Simulated Secondary Click toggle to
   ON.

   The Acceptance Delay setting
   appears.
4. (Optional) Use the Acceptance Delay slider to adjust the
   length of time the primary button needs to be held down for (before its release)
   to perform the simulated secondary click.

For more information about configuring Click Assist, view GNOME
help pages (see [Viewing GNOME Help](accessibility-AccessingAssistiveTechnologies.html#viewing-gnome-help) for information on how to view the help pages).

### Configurable Settings of Click Assist

The following table provides an overview of the settings that can be configured for
the Click Assist group of settings.

Table 3-6 Click Assist Settings

| Setting | Description |
| --- | --- |
| Simulated Secondary Click | Enables you to perform a secondary click (usually the right mouse button) by holding down the primary button for a length of time and then releasing it.  The related setting Acceptance Delay is used to adjust the length of time you need to hold the primary button down before releasing it. |
| Hover Click | Enables you to perform a mouse click by hovering the mouse pointer over the item to be clicked. The mouse does not have to be kept perfectly still while hovering the pointer as some movement is allowed. You can adjust the Motion Threshold setting to change the amount a mouse pointer can move and still be considered to be hovering. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/accessibility/accessibility-ConfiguringTypingAssistValues.html -->

## Customizing Typing Assist

Customize the Typing Assist group configurations of the Typing
settings that provide accessibility features, such as sticky keys and bounce
keys, to help with key presses.

The following example procedure provides the steps you need to perform to customize
the configurations of the Repeat Keys setting
(Repeat Keys is enabled by default).

1. Access the Accessibility panel by using
   a preferred method. 

   See [Accessing Assistive Technologies](accessibility-AccessingAssistiveTechnologies.html#ol-assistive-gnome).
2. Select Typing.

   The Typing panel of options appears.
3. On the Typing panel, in the Typing
   Assist section, select Repeat
   Keys.

   The Speed and Delay
   settings appear.
4. Use the Speed slider to speed at which key presses are
   repeated when a key is held down.
5. Use the Delay slider to adjust the length of time it
   takes before repeated key presses are actioned (increasing the
   Delay gives you more time to release a key before
   repeated key presses start),
6. (Optional): Open a text editor and hold down a key to see if further
   adjustments are needed.

For more information about configuring Typing Assist, view
GNOME help pages (see [Viewing GNOME Help](accessibility-AccessingAssistiveTechnologies.html#viewing-gnome-help) for information on how to view the help
pages).

### Configurable Settings of Typing Assist

The following table provides an overview of the settings that can be configured for
the Typing Assist group of settings.

Table 3-7 Typing Assist Settings

| Setting | Description |
| --- | --- |
| Repeat Keys | With Repeat Keys enabled (the default) a held down key raises repeated key press events until the key is released.  The Delay setting can be adjusted to give users more time to release keys before repeated key presses start, and the Speed setting can be adjusted to change how quickly the key presses are repeated. You can also disable the Repeat Keys. |
| Sticky Keys | Enables shortcut keys to be typed in sequence instead of one key being held before the other key is pressed. |
| Slow Keys | Enabling Slow Keys sets a delay between a key being typed and the corresponding character being displayed on-screen. The Acceptance Delay setting can be used to control the extent of the delay. |
| Bounce Keys | Enable this setting if you need the system to ignore inadvertent repetitive key presses that follow the initial intended key press.  The Acceptance Delay setting can be used to adjust the time interval during which a repeated key press is ignored. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/accessibility/accessibility-UsingBraille.html -->

## 4 Using Braille

Braille support is included in the GNOME desktop's accessibility features. Likewise, the
`brltty` daemon that's running as a background process enables users to
access information on Braille display devices.


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/accessibility/accessibility-ConfiguringtheBRLTTYService.html -->

## Installing and Customizing the brltty Service

Support for a Braille device is provided by the BRLTTY daemon
(`brltty`). You configure this service through the
`/etc/brltty.conf` configuration file.

Note:

The `brltty` service isn't available by default. To use this service you
must install the `brltty` package.

1. Install the `brltty` package.

   ```
   sudo dnf install -y brltty
   ```
2. Configure settings in `/etc/brltty.conf` as needed.

   See [Configurable Settings of the brltty Service](accessibility-ConfiguringtheBRLTTYService.html#section_rkg_rbv_t5b).
3. Enable the `brltty` service. 

   ```
   sudo systemctl enable --now brltty
   ```
4. Reboot the system.
5. Verify that the brltty service is running.

   After the system reboots, verify that the service is running, as follows:

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
Orca. To configure Braille options in the Screen Reader, see [Configuring Braille Options on the Screen Reader](accessibility-ConfiguringBrailleOptionsontheScreenReader.html#braille-screenrdr "Use the Braille tab on the GNOME desktop's Screen Readers Preferences window to configure Braille options.").

For more information, see the `brltty(1)` manual page.

### Configurable Settings of the brltty Service

The following table lists a selection of configurations that you can set in
`/etc/brltty.conf`:

Table 4-1 Configuration settings of the brltty service

| Functional Requirement | Configuration Setting |
| --- | --- |
| Authorize users who can use the Braille device. | Specify the users on the line `#api-parameters Auth=user:`, for example:   ``` api-parameters Auth=user:jsmith, jdoe, bbrown ``` |
| Authorize groups who can use the Braille device. | Specify the groups on the line `#api-parameters Aut=group:`. For example, for a group called `braille`, you would enter:   ``` api-parameters Auth=group:braille ``` |
| Specify the Braille display device driver. | Uncomment the appropriate `#braille-driver` line that contains the selected driver. Drivers are identified by two-letter codes, which are provided in the configuration file, for example:   ``` braille-driver vo ```   On a single `braille-driver` line, you can specify multiple, comma-separated drivers. In this case, the service automatically scans the list and detects the appropriate driver. |
| Specify the type of Braille display device. | Uncomment the appropriate `#braille-device` line that contains the selected device. Several lines that correspond to specific device types are provided, for example:   ``` braille-device bluetooth:address ```   On a single `braille-device` line, you can specify multiple, comma-separated devices. In this case, the service automatically scans the list and detects the appropriate device. |


---
<!-- page: https://docs.oracle.com/en/operating-systems/oracle-linux/10/accessibility/accessibility-ConfiguringBrailleOptionsontheScreenReader.html -->

## Configuring Braille Options on the Screen Reader

Use the Braille tab on the GNOME desktop's Screen Readers
Preferences window to configure Braille options.

Note:

You must perform the following steps as a non-root user.

1. Open the Screen Reader Preferences window.

   ```
   orca -s
   ```

   The `-s` option can also be typed as `--setup`. The
   command opens the Screen Reader Preferences window.

   Note:

   When you open the Screen Reader Preferences window, the screen
   reader is temporarily enabled so you can hear the effect each setting has. The
   temporary activation of the screen reader is disabled when you close the window and
   end the program by pressing `Ctrl+C`.
2. Select the Braille tab.
3. Customize the Braille options according to user needs.
4. Select Apply, and then Select OK.
5. At the command line, press `Ctrl+C` to return to the command
   prompt.

   The temporary activation of the screen reader is disabled.
6. Enable the screen reader.

   Access the Accessibility panel by using a
   preferred method. See [Accessing Assistive Technologies](accessibility-AccessingAssistiveTechnologies.html#ol-assistive-gnome)

   Select Seeing, and then switch the
   Screen Reader toggle to ON to enable the
   screen reader.

Note:

If you change settings in `/etc/brltty.conf`, then you must also restart
Orca. To configure `/etc/brltty.conf`, see [Installing and Customizing the brltty Service](accessibility-ConfiguringtheBRLTTYService.html#brltty "Support for a Braille device is provided by the BRLTTY daemon (brltty). You configure this service through the /etc/brltty.conf configuration file.").

### Configurable Braille Settings on the Screen Reader

On the Braille page, you can configure the following settings:

Display Settings
:   Defines how Braille is displayed.

Verbosity
:   Defines the amount of information rendered in Braille.

Selection and Hyperlink Indicators
:   Defines how selected text and hyperlinks are displayed.

Flash Message Settings
:   Enables notifications and configures how these notifications are handled.

For more information about configuring Orca's Braille options, do the following:

- View the Orca help pages by selecting the Help option on the
  Screen Reader Preferences window (viewing the help pages
  requires a web browser).
- See <https://help.gnome.org/users/orca/stable/preferences_braille.html.en>