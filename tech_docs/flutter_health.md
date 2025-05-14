Guide: Using the health Flutter Package to Access Health Connect and Apple Health
This guide teaches your AI assistant how to use the health Flutter package to read and write health data on both Android (Google Health Connect) and iOS (Apple Health). It covers setup, permissions, reading, writing, and deleting health data, with practical Dart code examples.

Setup
1. Add the Dependency
Add the package to your pubspec.yaml:

text
dependencies:
  health: ^12.2.0
Run flutter pub get to install.

2. Platform-Specific Configuration
iOS (Apple Health)
Add these keys to ios/Runner/Info.plist:

xml
<key>NSHealthShareUsageDescription</key>
<string>We will sync your data with the Apple Health app to give you better insights</string>
<key>NSHealthUpdateUsageDescription</key>
<string>We will sync your data with the Apple Health app to give you better insights</string>
In Xcode, enable the "HealthKit" capability for your app target.

Android (Health Connect)
The user must have the Health Connect app installed.

No additional manifest entries are required for basic use.

Basic Usage
1. Initialize and Configure
dart
import 'package:health/health.dart';

final health = Health();

void main() async {
  // Always configure before use
  await health.configure();
}
2. Request Permissions
Before accessing health data, request the appropriate permissions:

dart
var types = [
  HealthDataType.STEPS,
  HealthDataType.BLOOD_GLUCOSE,
];

// Request access to the data types
bool requested = await health.requestAuthorization(types);
For both read and write permissions:

dart
var permissions = [
  HealthDataAccess.READ_WRITE,
  HealthDataAccess.READ_WRITE,
];

bool requested = await health.requestAuthorization(types, permissions: permissions);
3. Reading Health Data
Fetch health data points for a time range:

dart
var now = DateTime.now();
var yesterday = now.subtract(Duration(days: 1));

List<HealthDataPoint> healthData = await health.getHealthDataFromTypes(
  yesterday,
  now,
  types,
);

// Example: print each data point
for (var point in healthData) {
  print('${point.typeString}: ${point.value} (${point.unitString})');
}
Get Total Steps for Today
dart
var midnight = DateTime(now.year, now.month, now.day);

int? steps = await health.getTotalStepsInInterval(midnight, now);
print('Total steps today: $steps');
4. Writing Health Data
Add new health data (e.g., steps or blood glucose):

dart
bool success = await health.writeHealthData(
  10, // value
  HealthDataType.STEPS,
  now,
  now,
);

success &= await health.writeHealthData(
  3.1, // value
  HealthDataType.BLOOD_GLUCOSE,
  now,
  now,
);
Specify the recording method (optional):

dart
success &= await health.writeHealthData(
  10,
  HealthDataType.STEPS,
  now,
  now,
  recordingMethod: RecordingMethod.manual,
);
5. Deleting Health Data
Delete data of a given type for a time range:

dart
var earlier = now.subtract(Duration(hours: 24));
bool success = await health.delete(
  type: HealthDataType.STEPS,
  startTime: earlier,
  endTime: now,
);
Delete by UUID (if you have it):

dart
String uuid = healthData.first.uuid;
bool success = await health.deleteByUUID(
  type: HealthDataType.STEPS,
  uuid: uuid,
);
6. Filtering by Recording Method
Fetch only manually entered or unknown data:

dart
List<HealthDataPoint> manualData = await health.getHealthDataFromTypes(
  types: [HealthDataType.STEPS],
  startTime: yesterday,
  endTime: now,
  recordingMethodsToFilter: [RecordingMethod.manual, RecordingMethod.unknown],
);
Best Practices & Notes
Health Connect Requirement: On Android, Health Connect must be installed for the plugin to work.

Permissions: Always check and request permissions before reading or writing data.

Platform Differences: Some health data types or features may only be available on iOS or Android.

Error Handling: Always handle exceptions as some operations may fail if permissions are missing or data is unavailable.

Data Privacy: Only access the data types your app truly needs.

References
health package documentation and example
https://pub.dev/packages/health
GitHub example
https://github.com/HTD-Health/flutter-health-plugin