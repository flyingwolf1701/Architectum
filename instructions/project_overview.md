\| **Web App (MVP)** | Full workout setup, movement selection, level progression, and point tracking |
\| **Phone App (Stretch Goal)** | Dedicated UI, timer customization, point history, streak tracking |
\| **Watch App (Further Stretch Goal)** | Quick start, view current level, log reps/time, navigate levels, view last session summary |**Product Overview: Qapla' Fitness (Updated)**

Qapla' Fitness helps users build consistent, sustainable fitness habits through adaptive movement flows, breath-led intent, and a gamified reward system. Designed to minimize friction and maximize presence, the app rewards users for simply starting and guides them through bodyweight or machine-based workouts that scale with skill and confidence.

The MVP is delivered as a web app with a future roadmap toward Android phone and watch integration. Initial focus is on Calisthenics and Gym Machines. Future expansions include additional workout types, recovery tools, and new progression formats.

---

## **Workout Philosophy**

* **Starting is the win**: Users earn high-value points for simply beginning their session.
* **Progress through adaptability**: Movements scale up/down within a session; regressions are embraced, not punished.
* **Structure with freedom**: Users can change movement order, modify difficulty, or reattempt.
* **Whole-body design**: Every session incorporates core, fascia work, and at least two additional movement groups.
* **Low friction, high reward**: Clean UI, minimal input required, and clear progress tracking.

---

## **Key Features**

### ✅ **Gamified Point System**

* +500 pts: Starting the workout
* +100 pts: Each warm-up or movement group started
* +1 pt per rep or second of active work
* Bonus points for higher-level completions
* *Points are only visible on phone (not watch)*

### ✅ **Progressive Movement Engine**

* Default movement target: 50 reps (or time-based equivalent)
* Adaptive block design:

  * Start with warm-up of 10 at **Level N-2 and 10 at Level N-1**

    * if N-2 or N-1 are less then one then it is level 1
  * Continue with as many reps as possible at **Level N**
  * If not enough to hit the target, regress via **Decrease Row** through lower levels
  * Hitting the full target (any mix of levels) = **Victory**
  * Completing Level N's full segment (without decrease) unlocks **Level N+1** for future sessions
* Controls: **⬆ Up**, **⬇ Down**, **✅ Done** to end block

### ✅ **Machine-Based Adaptation**

* Each level corresponds to a weight range
* UI matches the calisthenics flow: up/down to adjust load, done to complete
* Reps are still tracked to contribute toward the target goal

---

## **MVP User Flow**

### 🔹 Login / Launch App

### 🔹 Screen 1: Choose Focus

* \[✓] Workout Type

### 🔹 Screen 2: Select Workout Type

* (✓) Calisthenics
* (Coming Soon)Machines, Kettlebells, Dumbbells, Barbells, Animal Flow, Aerial, Original Strength, Fascia Therapy

### 🔹 Screen 3: Choose Workout(s)

* \[✓] Warm-up (blocking, back anchor)
* \[✓] Core (included daily)
* \[✓] Select 1–2 additional movements
* \[✓] Start 

---

## **Workout Session Flow**

### 1. Warm-Up

* Block therapy
* Back Anchor
* Bridge
* plank
* cardio

### 2. Main Workout

* Adaptive progression model with table UI:

  * **Action** (Warm-up or Workout)
  * **#** (reps completed)
  * **Level** (progressive level or direction: up/down)
* Flow:

  * Start two levels below current
  * Work up through current level
  * If target not met, drop down levels and continue
  * Any combination completing target = valid
  * Full completion at current level unlocks next level

---

## Calisthenics Movement Progressions

\---

\### 🔹 Push Progression (Push-Ups)

1\. Wall Push-Ups &#x20;

2\. Incline Push-Ups (high surface) &#x20;

3\. Knee Push-Ups &#x20;

4\. Full Push-Ups &#x20;

5\. Decline Push-Ups (feet elevated) &#x20;

6\. Diamond Push-Ups &#x20;

7\. Archer Push-Ups &#x20;

8\. Clap Push-Ups (explosive) &#x20;

9\. One-Arm Assisted Push-Ups &#x20;

10\. Full One-Arm Push-Ups &#x20;

\---

\### 🔹 Pull Progression (Pull-Ups)

1\. Dead Hangs &#x20;

2\. Scapular Pull-Ups &#x20;

3\. Assisted Pull-Ups (band or machine) &#x20;

4\. Negative Pull-Ups &#x20;

5\. Jumping Pull-Ups &#x20;

6\. Half Pull-Ups &#x20;

7\. Full Pull-Ups &#x20;

8\. Close-Grip Pull-Ups &#x20;

9\. Wide-Grip Pull-Ups &#x20;

10\. Muscle-Ups &#x20;

\---

\### 🔹 Dips Progression

1\. Bench Dips (feet on floor) &#x20;

2\. Bench Dips (feet elevated) &#x20;

3\. Parallel Bar Support Hold &#x20;

4\. Assisted Dips (band/machine) &#x20;

5\. Negative Dips &#x20;

6\. Full Dips &#x20;

7\. Ring Dips &#x20;

8\. Korean Dips (forward lean) &#x20;

9\. Weighted Dips &#x20;

10\. Straight Bar Dips &#x20;

\---

\### 🔹 Legs Progression (Squats)

1\. Chair Squats &#x20;

2\. Assisted Squats &#x20;

3\. Bodyweight Squats &#x20;

4\. Wide-Stance Squats &#x20;

5\. Narrow-Stance Squats &#x20;

6\. Bulgarian Split Squats &#x20;

7\. Pistol Squats with Support &#x20;

8\. Pistol Squats (unassisted) &#x20;

9\. Jump Squats &#x20;

10\. Shrimp Squats &#x20;

\---

\### 🔹 Core Progression (Leg Raises)

1\. Lying Knee Raises &#x20;

2\. Lying Leg Raises &#x20;

3\. Hanging Knee Raises &#x20;

4\. Hanging Leg Raises &#x20;

5\. Toes-to-Bar &#x20;

6\. L-Sit (floor or bar) &#x20;

7\. Hanging Windshield Wipers &#x20;

8\. Dragon Flags &#x20;

9\. V-Ups &#x20;

10\. Front Lever Holds &#x20;

---

## **App Tools & Utilities**

### ⏱️ Countdown & Beep Timer

* Optional stopwatch-style countdown for warm-ups and holds
* Configurable beep intervals (e.g., every 1 min, every 3 min, or custom)

## **Future-Proofing**

* **Workout Types**: Kettlebells, Dumbbells, Barbells, Animal Flow, Aerial, Original Strength, Fascia Therapy (displayed but disabled)
* **Movement Groups**: Push, Pull, Legs, Core, Inversion, Mobility (UI displayed but disabled)
* **Cooldowns**: UI present as placeholder
* **Stretch Goals**: Social rewards, shareable streaks, fascia/mobility programming, advanced audio cues
