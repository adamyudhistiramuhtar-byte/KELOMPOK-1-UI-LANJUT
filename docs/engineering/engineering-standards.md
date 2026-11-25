# Engineering standards

These rules apply to every developer and coding tool. Work only on an assigned issue with a clear scope, readiness and dependency review. Coordinate cross-workstream changes with the accountable person; architecture, design tokens and API contract changes require relevant owners' review. Never bypass hooks/checks, force push, self-approve, invent tests or approvals, publish unapproved personal data or credentials, or declare Done before the agreed Definition of Done. A tool review does not replace an independent human peer review.

## Product and design
Use the approved design foundation and shared tokens; no parallel design system or visual values in components. UI implementation waits for the required design gate. Preserve people-first editorial direction, white/navy, EB Garamond and Inter; accessible semantic markup, keyboard focus, responsive layouts and reduced motion are required. WCAG 2.2 AA is a target, not a compliance claim without testing.

## Code and data
Use readable, modular code, explicit contracts and proportionate reuse. Avoid unused code, unhandled errors, unsafe casts, arbitrary lint suppression and debug output. API client, transformation, state and rendering should be separated; support loading, success, empty, error and retry. Mocks are labelled and do not prove real API integration. Never expose secrets in frontend bundles. Dependencies require review of need, compatibility, maintenance, licence, security and bundle impact. Stack and package manager are not yet agreed.

## Naming and comments
Components and types use PascalCase; functions, variables and composables use camelCase; true constants use UPPER_SNAKE_CASE; directories use kebab-case. Follow the actual framework conventions once agreed. Code comments use English and explain non-obvious reasons or constraints, not conversations; TODO requires an issue reference. Preserve required copyright and attribution. Do not rename other members' work without coordination.

## Authority and review
Adam coordinates project scope and integration; Alexius owns foundation, Sindi design, Marza profile/contact, Panji API/data and Indra project showcase. CODEOWNERS names multiple eligible reviewers only for existing paths. It is a routing aid, not proof of review or a replacement for human approval. Follow academic disclosure requirements for permitted tool assistance.
