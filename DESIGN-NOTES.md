# Design revision

The 17-slide presentation was redesigned using the user's supplied Apple design guide.

- Neutral white, #f5f5f7 and #272729 surfaces; blue reserved for interactive controls.
- Embedded Pretendard Regular and SemiBold, with the SIL Open Font License included in the standalone HTML.
- New book cover image, monochrome donut chart, paired career routes, open editorial columns, and quieter navigation.
- Existing presentation controls, keyboard navigation, document enlargement and reduced-motion support retained.
- Original version preserved in `previous-design`.

## Hero asset

File: `assets/hero-book.png`

Generated with the built-in image generation tool. Final prompt: "Use case: product-mockup. Create one ultra-refined editorial studio product photograph for a Korean career counseling presentation website, inspired by the restraint of Apple product photography. Main subject: a single elegant white unprinted open book lying on a pure seamless off-white (#f5f5f7) studio surface, with two sculptural broad paper pages rising and gently diverging into two clean flowing paths to suggest education and employment, believable premium paper texture and precise edges. No other objects. Wide landscape 3:2 composition, camera close at low three-quarter frontal angle. Object centrally composed, ample breathing room, mostly lower-middle frame, softly directional daylight, extremely subtle natural contact shadow. White-on-white, a hint of silver-gray on folded paper edges. No colorful lighting, no gradients as graphics, no neon, no rings, no people, no text, no logos, no decorative graphics. This is a photographic hero asset, not a website mockup. Visually sophisticated, calm, premium, crisp, physically plausible paper."

## Editing

Edit `index.html` for content or behavior; edit `design-v2.css` for the visual system. Run `package-html.py` to synchronize the CSS and bundle the assets into `특성화고_진로진학상담.html`. `redesign.py` is the original migration, not the build command.
