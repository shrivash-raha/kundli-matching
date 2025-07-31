import { useState } from "react";

function InputForm({ onSubmit }) {
  const [girl, setGirl] = useState({ dob: "", tob: "", place: "" });
  const [boy, setBoy] = useState({ dob: "", tob: "", place: "" });

  const handleChange = (e, person, setPerson) => {
    const { name, value } = e.target;
    setPerson({ ...person, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ girl, boy });
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Girl's Details</h2>
      <input
        type="date"
        name="dob"
        value={girl.dob}
        onChange={(e) => handleChange(e, girl, setGirl)}
        required
      />
      <input
        type="time"
        name="tob"
        value={girl.tob}
        onChange={(e) => handleChange(e, girl, setGirl)}
        required
      />
      <input
        type="text"
        name="place"
        value={girl.place}
        onChange={(e) => handleChange(e, girl, setGirl)}
        placeholder="Place of Birth"
        required
      />

      <h2>Boy's Details</h2>
      <input
        type="date"
        name="dob"
        value={boy.dob}
        onChange={(e) => handleChange(e, boy, setBoy)}
        required
      />
      <input
        type="time"
        name="tob"
        value={boy.tob}
        onChange={(e) => handleChange(e, boy, setBoy)}
        required
      />
      <input
        type="text"
        name="place"
        value={boy.place}
        onChange={(e) => handleChange(e, boy, setBoy)}
        placeholder="Place of Birth"
        required
      />

      <br />
      <button type="submit">Calculate</button>
    </form>
  );
}

export default InputForm;
