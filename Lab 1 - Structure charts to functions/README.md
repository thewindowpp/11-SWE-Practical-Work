# Lab 523: Enhancing Web Accessibility

## Overview
In this lab, you will **improve the accessibility** of the **museum exhibit webpage** you created in the previous lab. Your goal is to make the page **easier to navigate, readable for screen readers, and visually accessible**.

## Objectives
- Implement **ARIA roles** to improve screen reader compatibility.
- Ensure **keyboard navigation** works properly.
- Improve **color contrast** for readability.
- Use **alt text** to make images accessible.
- Apply **best practices for accessible forms**.

---

## Step 1: Audit the Existing Page
Before making changes, **identify accessibility issues** using:

1. **[WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/)**
2. **Keyboard Testing**:
    - Use **Tab, Shift+Tab, Enter, and Spacebar** to navigate.
    - Check that all interactive elements **receive focus**.
3. **Screen Reader Testing** (if available):
    - Use **NVDA**, **VoiceOver**, or **ChromeVox** to listen to the webpage.

---

## Step 2: Implement Accessibility Enhancements

### 2.1 **Improve Page Structure with ARIA Landmarks**
Add **ARIA roles** to clearly define sections for screen readers.

```html
<header role="banner">
    <h1>The Wonders of Ancient Egypt</h1>
</header>

<nav role="navigation">
    <ul>
        <li><a href="#highlights">Key Highlights</a></li>
        <li><a href="#details">Exhibit Details</a></li>
        <li><a href="#extras">Explore More</a></li>
        <li><a href="#contact">Contact Us</a></li>
    </ul>
</nav>

<main role="main">
    <section id="highlights">
        <h2>Key Highlights</h2>
        <ul>
            <li>The Great Pyramids and their construction</li>
            <li>The discovery of King Tutankhamun's tomb</li>
            <li>Daily life in ancient Egyptian society</li>
        </ul>
    </section>

    <footer role="contentinfo">
        <h2>Contact Us</h2>
        <p>Email: <a href="mailto:info@nationalhistorymuseum.com">info@nationalhistorymuseum.com</a></p>
        <p>Phone: (123) 456-7890</p>
    </footer>
</main>
```

---

### 2.2 **Improve Keyboard Navigation**
Ensure interactive elements **receive focus** and have a clear **focus outline**.

```css
a:focus, button:focus {
    outline: 2px solid #ffcc00;
}
```

If navigation relies on dropdowns, students should implement **keyboard-accessible menus**:

```css
nav ul li {
    display: inline-block;
    position: relative;
}

nav ul li:focus-within ul {
    display: block;
}
```

---

### 2.3 **Improve Color Contrast**
Use [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) to ensure **text is readable**.

```css
body {
    color: #222;
    background-color: #f9f9f9;
}

button {
    background-color: #0055a4;
    color: white;
}

button:hover {
    background-color: #003366;
}
```

Ensure text color **has at least a 4.5:1 contrast ratio** against the background.

---

### 2.4 **Add Alt Text for Images**
All images should have **descriptive alt text**.

```html
<img src="pyramid.jpg" alt="A view of the Great Pyramid of Giza under a blue sky">
```

For **decorative images**, use an **empty alt attribute** to hide them from screen readers.

```html
<img src="border-design.png" alt="">
```

---

### 2.5 **Ensure Form Accessibility**
All forms should:

✅ Have **labels associated** with inputs.

```html
<label for="email">Email Address:</label>
<input type="email" id="email" name="email" required>
```

✅ Use **aria-live** for error messages.

```html
<p id="error-message" aria-live="polite">Please enter a valid email.</p>
```

---

## Step 3: Validate and Test Your Page
After implementing the fixes, **retest your page** using:

- **[WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/)**
- **Keyboard navigation**
- **Screen reader testing (if available)**

---

## Assessment Criteria
- Proper use of ARIA roles and landmarks	5
- Keyboard navigation and focus indicators	5
- High-contrast color scheme and readable text	5
- Descriptive alt text for images	5
- Accessible forms with labels and error messages

---

## Extensions
- **Make the website fully responsive** using CSS media queries.
- **Implement a skip navigation link** for screen reader users.
- **Enhance the navigation menu with ARIA attributes**:

```html
<nav role="navigation" aria-label="Main Navigation">
```

---