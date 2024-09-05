import React, { useState, useEffect } from 'react';
import axios from 'axios';

interface Measurement {
  id: number;
  value: number;
  timestamp: string;
}

function App(): JSX.Element {
  const [measurements, setMeasurements] = useState<Measurement[]>([]);
  const [latestMeasurement, setLatestMeasurement] = useState<Measurement | null>(null);

  useEffect(() => {
    fetchMeasurements();
    fetchLatestMeasurement();
    // 10秒ごとにデータを更新
    const interval = setInterval(() => {
      fetchMeasurements();
      fetchLatestMeasurement();
    }, 100);
    return () => clearInterval(interval);
  }, []);

  const fetchMeasurements = async (): Promise<void> => {
    try {
      const response = await axios.get<Measurement[]>('http://localhost:8000/measurements/');
      setMeasurements(response.data);
    } catch (error) {
      console.error('Error fetching measurements:', error);
    }
  };

  const fetchLatestMeasurement = async (): Promise<void> => {
    try {
      const response = await axios.get<Measurement>('http://localhost:8000/measurements/latest/');
      setLatestMeasurement(response.data);
    } catch (error) {
      console.error('Error fetching latest measurement:', error);
    }
  };

  return (
    <div className="App">
      <h1>測定値一覧</h1>
      <h2>最新の値</h2>
      {latestMeasurement ? (
        <p>Value: {latestMeasurement.value}, Time: {new Date(latestMeasurement.timestamp).toLocaleString()}</p>
      ) : (
        <p>No latest measurement available</p>
      )}
      <h2>履歴</h2>
      <ul>
        {measurements.map((measurement: Measurement) => (
          <li key={measurement.id}>
            Value: {measurement.value}, Time: {new Date(measurement.timestamp).toLocaleString()}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;