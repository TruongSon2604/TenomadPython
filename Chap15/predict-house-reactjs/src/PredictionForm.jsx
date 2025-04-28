import React, { useState } from "react";
import "./PredictionForm.scss";

const DEFAULT_VALUES = {
  MedInc: 4.5,
  HouseAge: 20,
  AveRooms: 6,
  AveOccup: 3,
  Latitude: 37.88,
  Longitude: -122.23,
  AveHouseVal: 2.5,
};

function PredictionForm() {
  const [form, setForm] = useState(DEFAULT_VALUES);
  const [result, setResult] = useState("");
  const [rmse, setRmse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.id]: parseFloat(e.target.value) });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResult("");
    try {
      const res = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });
      if (!res.ok) throw new Error("Lỗi khi gọi API");
      const data = await res.json();
      setResult(`Giá nhà dự đoán: $${data.prediction?.toFixed(2)} nghìn USD`);
      setRmse(`Độ chính xác của mô hình: ${data.model_rmse?.toFixed(2)}`);
    } catch (error) {
      setResult("Lỗi khi gọi API");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div id="frm">
      <form id="prediction-form" onSubmit={handleSubmit}>
        <h2>Dự đoán giá nhà California </h2>
        <label>MedInc:</label>
        <input
          type="number"
          placeholder="Thu nhập trung bình (10k USD)"
          step="any"
          id="MedInc"
          required
          value={form.MedInc}
          onChange={handleChange}
        />

        <label>HouseAge:</label>
        <input
          type="number"
          placeholder="Tuổi của nhà"
          step="any"
          id="HouseAge"
          required
          value={form.HouseAge}
          onChange={handleChange}
        />

        <label>AveRooms:</label>
        <input
          type="number"
          step="any"
          id="AveRooms"
          required
          value={form.AveRooms}
          onChange={handleChange}
        />

        <label>AveOccup:</label>
        <input
          type="number"
          step="any"
          id="AveOccup"
          required
          value={form.AveOccup}
          onChange={handleChange}
        />

        <label>Latitude:</label>
        <input
          type="number"
          step="any"
          id="Latitude"
          required
          value={form.Latitude}
          onChange={handleChange}
        />

        <label>Longitude:</label>
        <input
          type="number"
          step="any"
          id="Longitude"
          required
          value={form.Longitude}
          onChange={handleChange}
        />

        <label>AveHouseVal:</label>
        <input
          type="number"
          step="any"
          id="AveHouseVal"
          required
          value={form.AveHouseVal}
          onChange={handleChange}
        />
        <div id="result">{result}</div>
        <div id="rmse">{rmse}</div>
        <button type="submit" disabled={loading}>
          {loading ? "Đang dự đoán..." : "Dự đoán"}
        </button>
      </form>
    </div>
  );
}

export default PredictionForm;
